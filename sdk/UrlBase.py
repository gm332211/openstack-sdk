import urllib
import urllib2
import json
def url_request(url,data=None,headers=None):
    if not headers:
        headers = {
            "Content-type": "application/json",
        }
    if data:
        req = urllib2.Request(url=url, data=json.dumps(data), headers=headers)
    else:
        req = urllib2.Request(url=url, headers=headers)
    response=urllib2.urlopen(req)
    return response
def get_token():
    url = 'http://172.30.14.10:35357/v3/auth/tokens'
    DOMAIN = 'demo'
    PROJECT = 'admin'
    USERNAME = 'admin'
    PASSWORD = '0000000'
    data = {"auth": {"identity": {"methods": ["password"],
                                    "password": {"user": {"name": USERNAME, "password": PASSWORD,
                                                          "domain": {"name": DOMAIN}}}},
                       "scope": {"project": {"name": PROJECT, "domain": {"name": DOMAIN}}}}}
    response = url_request(url=url,data=data)
    token=response.headers.get('X-Subject-Token')
    return token
def get_users():
    url = 'http://172.30.14.10:35357/v3/users'
    headers={
        "Content-type": "application/json",
        "X-Auth-Token": get_token(),
    }
    response = url_request(url=url, headers=headers)
    data=response.read()
    return json.loads(data)
print(get_users())
