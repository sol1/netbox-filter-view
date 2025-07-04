from netbox.plugins import PluginMenu, PluginMenuItem


menu = PluginMenu(
    label='Filter View',
    groups=(
        (
            'Filter View', [
                PluginMenuItem(
                    link='plugins:netbox_filter_view:filter_view',
                    link_text='Filter View',

                )
            ]
        ),
    ),
    icon_class='mdi mdi-database-eye-outline'
)