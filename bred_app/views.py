from netbox.views import generic
import logging
from dcim.models import Device
from dcim.tables import DeviceTable
from virtualization.models import VirtualMachine
from virtualization.tables import VirtualMachineTable
from . import forms, models, tables
from django.db.models import Q


class BredApplicationView(generic.ObjectView):
    queryset = models.BredApplication.objects.all()

    def get_extra_context(self, request, instance):
        tags = instance.tags.all()
        if len(tags) > 0:
            query = Q()
            for tag in instance.tags.all():
                query |= Q(tags=tag.id)
            machines_items = VirtualMachine.objects.filter(query)
            taggeditem_table = VirtualMachineTable(data=machines_items, orderable=False)

            devices_items = Device.objects.filter(query)
            taggeddevices_table = DeviceTable(data=devices_items, orderable=False)
        else:
            machines_items = VirtualMachine.objects.none()
            taggeditem_table = VirtualMachineTable(data=machines_items, orderable=False)

            devices_items = Device.objects.none()
            taggeddevices_table = DeviceTable(data=devices_items, orderable=False)
        taggeditem_table.configure(request)
        taggeddevices_table.configure(request)

        return {
            "machines_table": taggeditem_table,
            "devices_table": taggeddevices_table,
        }


class BredApplicationListView(generic.ObjectListView):
    queryset = models.BredApplication.objects.all()
    table = tables.BredApplicationTable


class BredApplicationEditView(generic.ObjectEditView):
    queryset = models.BredApplication.objects.all()
    form = forms.BredApplicationForm


class BredApplicationDeleteView(generic.ObjectDeleteView):
    queryset = models.BredApplication.objects.all()
