from netbox.filtersets import NetBoxModelFilterSet
from .models import BredApplicationRule


class AccessListRuleFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = AccessListRule
        fields = ("id", "access_list", "index", "protocol", "action")

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
