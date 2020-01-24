from rest_framework import serializers
from .models import Fixture
from .models import Account,PicFixture


class FixtureSerializer(serializers.ModelSerializer):


    class Meta:
        model = Fixture
        fields = ('pmddate','fixtureno','modelname','pmddate','usagelimit','usagecount','fixturegroup','storage','productionline','addby','description','te')



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('aname','fname')


class PicFixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PicFixture
        fields = ('fixtureno','fixturepicture')
