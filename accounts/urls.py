from rest_framework import routers
from .views import GroupViewSet,UserViewSet

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)
