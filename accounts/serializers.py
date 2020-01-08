from django.contrib.auth.models import User, Group
from rest_framework import serializers,permissions
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.serializers import UserSerializer as BaseUserViewsSerializer
from django.db import IntegrityError

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    # groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    class Meta(BaseUserRegistrationSerializer.Meta):
        print("hello1")
        fields = ('username', 'first_name', 'last_name', 'password','groups')

    # def create(self, validated_data):
    #     groups_data = validated_data.pop('groups')
    #     user = User.objects.create(**validated_data)
    #     for group_data in groups_data:
    #         # Group.objects.create(user=user, **group_data)
    #         # user.groups.add(1)
    #         user.groups.set(1)
    #     return user
    # def create(self, validated_data):
    #     try:
    #         user = self.perform_create(validated_data)
    #         user.groups.add(1)
    #
    #     except IntegrityError:
    #         self.fail("cannot_create_user")
    #
    #     return user
    def create(self, validated_data):
        try:
            groups_data = validated_data.pop('groups')
            print("---------------------hello-------------------")
            print(validated_data)
            print(groups_data.id)
            user = self.perform_create(validated_data)
            user.save()
            user.groups.add(1)

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

