from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem


filterview_buttons = [
    PluginMenuButton(
        link='plugins:netbox_filter_view:filterview_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    ),
]

filterview_items = (
    PluginMenuItem(
        link='plugins:netbox_filter_view:filterview_list',
        link_text='Filter Views',
        buttons=filterview_buttons,
    ),
)

menu = PluginMenu(
    label='Filter View',
    groups=(('Filter View', filterview_items),),
    icon_class='mdi mdi-database-eye-outline',
)
