from sdk import Openstack
op=Openstack.Openstack()
data=op.list_servers(host='openstack',fields='id')
flavor_data=op.list_flavor()
print(data)
