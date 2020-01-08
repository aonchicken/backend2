"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from accounts.urls import router
from fixture.urls import router as fixtures_router
from accounts.urls import router as accounts_router
from rest_framework_simplejwt import views as jwt_views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Fixture API')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('docs/', schema_view),
    path('', schema_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token-auth/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh-auth/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include(accounts_router.urls)),
    path('fixtures/', include(fixtures_router.urls)),
    # path to djoser end points
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]

