# Netbox Filter View
Netbox Filter View is a simple plugin that lets you create a url to return multiple objects, define the columns to display, grouping the returned objects by a value (eg: tenant), add sensible links to all the data and returns the data in datatables.

# URL Paramaters
URL Paramaters are used to define the filter views, they can be saved and shared externaly.

The example below gets all Virtual Machines and Devices that have the tag "switch" for the customer "acme", the tables that are generated are groups by site name and the listed fields in order are included in the table.
```
?api_path=/api/virtualization/virtual-machines/&api_path=/api/dcim/devices/&result_keys=custom_fields.InternalName,device_type.model,primary_ip.address,custom_fields.URL,comments,name,site.name,rack.name,position&table_groups=site.name&tag=switch&tenant=acme
```

## `api_path`
This paramater can be repeated causing filter view to load the data from multiple objects. 
The value is the API path for the object you want to load.

```
?api_path=/api/virtualization/virtual-machines/&api_path=/api/dcim/devices/
```

## `result_keys`
This paramater defines the columns and their order for all tables in the view. 
The value is a comma seperated list of values which matches keys returned by the `api_path`(s). For nested values dot notation can be used.

```
&result_keys=custom_fields.InternalName,device_type.model,primary_ip.address,custom_fields.URL,comments,name,site.name,rack.name,position
```

## `table_groups`
This paramater is used to define grouping. The data returned by the `api_path` is broken up into seperate tables with the data from each tables sharing the defined keys value. 
The value is a key in the returned data, for nested values dot notation can be used.

```
&table_groups=site.name
```
_In the example above the returned data would create one table per tenant_

## Any other paramaters
Any other paramaters added to the url are treated as filters for the `api_path`(s). They need to match Netbox's api paramaters.

```
&tag=switch&tenant=acme
```
