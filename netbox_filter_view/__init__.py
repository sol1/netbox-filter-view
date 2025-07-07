from netbox.plugins import PluginConfig


class NetBoxFilterViewConfig(PluginConfig):
    name = 'netbox_filter_view'
    verbose_name = 'NetBox Filter View'
    description = 'Provides a dynamic NetBox filter view page using API data.'
    version = '0.1.0'
    author = 'Dylan Lucci'
    base_url = 'filter-view'

config = NetBoxFilterViewConfig