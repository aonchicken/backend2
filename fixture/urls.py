from django.urls import path, include
from .views import FixtureViewSet
from .views import AccountViewSet,PicFixtureViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'fixtures', FixtureViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'picfixtures', PicFixtureViewSet)


