from rest_framework.views import APIView
from .models import Fixture
from .models import Account,PicFixture
from .serializers import FixtureSerializer
from .serializers import AccountSerializer,PicFixtureSerializer
from rest_framework import viewsets
from rest_framework.response import responses
from rest_framework.pagination import PageNumberPagination

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class SmallResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class FixtureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer
    pagination_class = SmallResultsSetPagination

class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    pagination_class = SmallResultsSetPagination

class PicFixtureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = PicFixture.objects.all()
    serializer_class = PicFixtureSerializer
    pagination_class = SmallResultsSetPagination


