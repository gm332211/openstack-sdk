from sdk import Openstack
op=Openstack.Openstack()
op.get_token()
op.test()
print(op.token)