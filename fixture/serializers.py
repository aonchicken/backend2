from rest_framework import serializers
from .models import Fixture


class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixture
        fields = ('pmddate','fixtureno','modelname','pmddate','usagelimit','usagecount','fixturegroup','storage','productionline','addby','description')