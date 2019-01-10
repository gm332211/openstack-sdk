# def identity_request(self, server, method, headers=None, body=None, type_return=None):
#     identity_url=openstack_setting.keystone_endpoint.get('url',None)
#     host, port = tools.partition_url(identity_url)
#     version=openstack_setting.keystone_endpoint.get('version',None)
#     url = identity_url + '/v' + str(version) + '/' + server
#     data = HttpBase.http_request(host=host, port=port, url=url, method=method, headers=headers, body=body,
#                         type_return=type_return)
#     return data