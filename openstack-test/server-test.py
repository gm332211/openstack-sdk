from sdk import Openstack
op=Openstack.Openstack()
data=op.show_server(id='b9c081a0-84bf-40b0-bced-9de232647810')
flavor_data=op.show_flavor(id=data['flavor']['id'])
print(flavor_data.get('vcpus'))