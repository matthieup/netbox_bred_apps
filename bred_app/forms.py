from netbox.forms import NetBoxModelForm
from .models import BredApplication
from extras.models import Tag
from utilities.forms.fields import CommentField, DynamicModelChoiceField


class BredApplicationForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = BredApplication
        fields = ("name", "description", "owner", "documentation", "tags")
