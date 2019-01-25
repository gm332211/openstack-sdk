#-*- coding:utf-8 -*-
# @Author:xiaoming
from sdk import Openstack
import json
op=Openstack.Openstack()
op.get_token()
data=op.create_image(image_name='test_image1',disk_format='qcow2',container_format='bare')
image_id=data.get('id',None)
f=open('files/cirros-0.3.6-x86_64-disk.img','rb')
data=f.read()
f.close()
if image_id:
    res=op.upload_image(image_id=str(image_id),image_file=data)
