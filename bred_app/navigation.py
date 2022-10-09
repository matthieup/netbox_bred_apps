from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

bredapplications_buttons = [
    PluginMenuButton(
        link="plugins:netbox_bred_apps:bredapplication_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
        color=ButtonColorChoices.GREEN,
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_bred_apps:bredapplication_list",
        link_text="Bred Applications",
        buttons=bredapplications_buttons,
    ),
)
