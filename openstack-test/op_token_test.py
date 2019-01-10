from sdk import Openstack
op=Openstack.Openstack()
op.get_token()
print(op.token)