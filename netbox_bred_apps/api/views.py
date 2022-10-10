from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers import BredApplicationSerializer


class BredApplicationViewSet(NetBoxModelViewSet):
    queryset = models.BredApplication.objects.all()
    serializer_class = BredApplicationSerializer
