import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import BredApplication


class BredApplicationTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = BredApplication
        fields = ("pk", "id", "name", "description", "owner", "documentation", "comments")
        default_columns = ("name", "description", "owner", "documentation", "comments")

    name = tables.Column(linkify=True)

    owner = ChoiceFieldColumn()
