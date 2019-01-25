#-*- coding:utf-8 -*-
# @Author:xiaoming
from sdk import Openstack
op=Openstack.Openstack()
data=op.list_image()
test=data.get('images')[0].get('container_format')