from extras.plugins import PluginConfig


class NetboxBredApps(PluginConfig):
    name = "netbox_bred_apps"
    verbose_name = "Bred Applications"
    description = "To store applications references"
    version = "0.2"
    base_url = "bred-applications"


config = NetboxBredApps
