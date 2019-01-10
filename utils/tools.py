import urllib,urlparse
from config import openstack_setting
def partition_url(url):
    """Separate host and port Function
    :param str url:Addresses that need to be separated
    """
    proto, rest = urllib.splittype(url)
    host, rest = urllib.splithost(rest)
    host, port = urllib.splitport(host)
    if port is None:
        port = 80
    return (host, port)
def auth_token(func):
    def inner(self,*args,**kwargs):
        if not self.token:
            self.get_token()
        data = func(self, *args, **kwargs)
        error_code = False
        try:
            error_code=data['error']['code']
        except:
            pass
        if error_code:
            self.get_token()
            data = func(self, *args, **kwargs)
        return data
    return inner
def url_filter(url,filter):
    filter_url='?'
    for key in filter:
        filter_url+=key+'='+filter[key]+'&'
    return urlparse.urljoin(url,filter_url)