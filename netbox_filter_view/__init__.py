from netbox.plugins import PluginConfig

from .version import __version__


class NetBoxFilterViewConfig(PluginConfig):
    name = 'netbox_filter_view'
    verbose_name = 'NetBox Filter View'
    description = 'Provides a dynamic NetBox filter view page using API data.'
    version = __version__
    author = 'Dylan Lucci'
    base_url = 'filter-view'
    min_version = '4.3.0'

config = NetBoxFilterViewConfig