from django.urls import path, include
from .views import FixtureViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'fixtures', FixtureViewSet)


