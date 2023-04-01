from django.urls import get_resolver
from rest_framework.viewsets import ViewSet

from TrickerTrust.settings import PLAYGROUND_CORE


class Methods1(ViewSet):
    @PLAYGROUND_CORE.parameters()
    def list(self, request):
        print(get_resolver().reverse_dict)

