# NetBox Filter View

NetBox Filter View is a simple plugin that allows you to create a URL to return multiple objects, define the columns to display, group the returned objects by a value (e.g. tenant), add sensible links to all the data, and return the data in DataTables.

# Installation

**Download the latest release**
```bash
cd /opt/netbox/plugins/
wget https://github.com/sol1/netbox-filter-view/releases/download/v0.1.5/netbox_filter_view-0.1.5.tar.gz
```
_Use the most appropriate repository for your installation._

**Add the plugin to `local_requirements.txt`**
```bash
cd /opt/netbox/
echo "netbox-filter-view @ file:///opt/netbox/plugins/netbox_filter_view-0.1.5.tar.gz" > local_requirements.txt
```

**Add the plugin to `configuration.py`**
```python
PLUGINS = ["netbox_filter_view"]
```

# URL Parameters

URL parameters are used to define the filter views. They can be saved and shared externally.

The example below retrieves all Virtual Machines and Devices that have the tag `switch` for the customer `acme`. The generated tables are grouped by site name, and the listed fields (in order) are included in the table.

```
api_path=/api/virtualization/virtual-machines/&api_path=/api/dcim/devices/&result_keys=custom_fields.InternalName,device_type.model,primary_ip.address,custom_fields.URL,comments,name,site.name,rack.name,position&table_groups=site.name&tag=switch&tenant=acme
```

## `api_path`

This parameter can be repeated, causing Filter View to load data from multiple objects.  
The value is the API path for the object you want to load.

```
api_path=/api/virtualization/virtual-machines/&api_path=/api/dcim/devices/
```

## `result_keys`

This parameter defines the columns and their order for all tables in the view. The value is a comma-separated list of keys matching the data returned by the `api_path`(s). 
Dot notation can be used for nested values.

```
&result_keys=custom_fields.InternalName,device_type.model,primary_ip.address,custom_fields.URL,comments,name,site.name,rack.name,position
```

## `table_groups`

This parameter is used to define grouping. The data returned by the `api_path` is split into separate tables, with each table being made up of data sharing the value of the defined key.  
Dot notation can be used for nested keys.

```
&table_groups=site.name
```

_In the example above, the returned data would be grouped into one table per site._

## Any other parameters

Any additional parameters added to the URL are treated as filters for the `api_path`(s).  
They must match NetBox’s API parameters.

```
&tag=switch&tenant=acme
```

# Development
Clone git repo to dev server, enable venv then cd to repo and pip install
```
ssh netbox-dev-server
git clone https://github.com/sol1/netbox-filter-view
```

```
ssh netbox-dev-server
cd /netbox-filter-view
source /netbox/install/path/venv/bin/activate 
pip install -e .
```