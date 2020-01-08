from django.contrib.auth.models import User, Group
from rest_framework import serializers,permissions
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.serializers import UserSerializer as BaseUserViewsSerializer
from django.db import IntegrityError
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions



class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    # groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    class Meta(BaseUserRegistrationSerializer.Meta):
        print("hello1")
        fields = ('username', 'first_name', 'last_name', 'password','groups')

    def validate(self, attrs):
        groups = attrs.pop("groups")
        user = User(**attrs)
        password = attrs.get("password")
        try:
            validate_password(password, user)
            attrs["groups"] = groups
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )

        return attrs
    def create(self, validated_data):
        try:
            groups_data = validated_data.pop('groups')
            user = self.perform_create(validated_data)
            user.save()
            user.groups.add(groups_data[0].id)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user







class UserViewsSerializer(BaseUserViewsSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id','username','email','first_name','last_name','groups','is_active','date_joined','groups','last_login', )

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'id' ,'name']

