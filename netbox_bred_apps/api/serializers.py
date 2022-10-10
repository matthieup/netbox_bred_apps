from rest_framework import serializers

from ipam.api.serializers import NestedPrefixSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import BredApplication


class NestedBredApplicationSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_bred_apps-api:bredapplication-detail"
    )

    class Meta:
        model = BredApplication
        fields = ("id", "url", "display", "name")


class BredApplicationSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_bred_apps-api:bredapplication-detail"
    )

    class Meta:
        model = BredApplication
        fields = ("id", "url", "display", "name", "description", "owner", "documentation")
