import httplib, json
from config import openstack_setting
def http_request(host, port, url, method, headers=None, body=None, type_return=None):
    """Protogenesis Http Function
    :param str host:The configuration USES the host address
    :param str(int) port:Configure to use the host port
    :param str url:Http request url
    :param str method:Http request method
    :param dict headers:Http request Headers
    :param dict body:Http request content
    :param str type_return: return type
    """
    conn = httplib.HTTPConnection(host=host, port=port)
    if not headers:
        headers = {
            "Content-type": "application/json",
        }
    request_dict = {'url': url, 'method': method, 'headers': headers}
    if method == 'POST' or method == 'PUT' or method=='PATCH':
        request_dict['body'] = json.dumps(body)
    print('%s %s'%(method,url))
    conn.request(**request_dict)
    res = conn.getresponse()
    if type_return == 'obj':
        return res
    return json.loads(res.read())