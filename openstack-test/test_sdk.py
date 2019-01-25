#-*- coding:utf-8 -*-
# @Author:xiaoming
from openstack import connection
AUTH_CONFIG = {
    'default': {
        # 'region_name': 'RegionOne',
        'auth': {
            'auth_url': 'http://192.168.1.10/identity',
            'username': 'admin',
            'password': 'password',
            'project_name': 'admin',
            'user_domain_name': 'Default',
            'project_domain_name': 'Default',
        },
        'compute_api_version': 2.1,
        'identity_api_version': 3,
        'identity_interface': 'admin',
    },
}
def Conn():
    return connection.Connection(
        **AUTH_CONFIG.get('default')
    )
conn=Conn()

conn.image.upload_image()