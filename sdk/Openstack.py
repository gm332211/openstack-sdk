import json
from sdk import HttpBase
from utils import tools
from config import openstack_setting


class Openstack(object):
    def __init__(self, domain=openstack_setting.DOMAIN, project=openstack_setting.PROJECT,
                 username=openstack_setting.USERNAME, password=openstack_setting.PASSWORD):
        self.domain = domain
        self.project = project
        self.username = username
        self.password = password
        self.token = None
        """Protogenesis Oenstack Class
        :param str domain:openstack domain name,default:openstack_setting.DOMAIN
        :param str project:openstack project name,default:openstack_setting.PROJECT
        :param str username:openstack username name,default:openstack_setting.USERNAME
        :param str password:openstack user password,default:openstack_setting.PASSWORD
        :param str token:openstack authentication token
        """

    @tools.auth_token
    def openstack_request(self, server, server_type, method, headers=None, body=None, filter=None, type_return=None):
        """Protogenesis Oenstack request
        :param str server:Access service address
        :param str server_type:Specify openstack service type
        :param str method:Specify access method
        :param dict headers:openstack reqeust headers
        :param dict body:openstack reqeust data
        :param str type_return:return openstack type
        """
        service = openstack_setting.openstack_endpoint.get(server_type, None)
        if service:
            service_url = service.get('url', None)
            version = service.get('version', None)
            host, port = tools.partition_url(service_url)
            url = service_url + '/v' + str(version) + '/' + server
            if filter:
                url = tools.url_filter(url, filter)
            if not headers:
                headers = {
                    "Content-type": "application/json",
                    "X-Auth-Token": self.token,
                }
            data = HttpBase.http_request(host=host, port=port, url=url, method=method, headers=headers, body=body,
                                         type_return=type_return)
            return data
        return False

    def identity_request(self, server, server_type, method, headers=None, body=None, type_return=None):
        """Protogenesis Oenstack request
        :param str server:Access service address
        :param str server_type:Specify openstack service type
        :param str method:Specify access method
        :param dict headers:openstack reqeust headers
        :param dict body:openstack reqeust data
        :param str type_return:return openstack type
        """
        service = openstack_setting.openstack_endpoint.get(server_type, None)
        if service:
            service_url = service.get('url', None)
            version = service.get('version', None)
            host, port = tools.partition_url(service_url)
            url = service_url + '/v' + str(version) + '/' + server
            if not headers:
                headers = {
                    "Content-type": "application/json",
                }
            data = HttpBase.http_request(host=host, port=port, url=url, method=method, headers=headers, body=body,
                                         type_return=type_return)
            return data
        return False

    def get_token(self):
        """Gets an openstack authentication token"""
        auth_dict = {"auth": {"identity": {"methods": ["password"],
                                           "password": {"user": {"name": self.username, "password": self.password,
                                                                 "domain": {"name": self.domain}}}},
                              "scope": {"project": {"name": self.project, "domain": {"name": self.domain}}}}}
        res = self.identity_request(server_type='identity', server='auth/tokens', method='POST', body=auth_dict,
                                    type_return='obj')
        if res:
            self.token = res.getheader('X-Subject-Token')
        else:
            self.token = None

    def list_domains(self, *args, **kwargs):
        """Get the domains list
        :param str filter:Filters the many.
        Request in request:
            :param str name:Filters the response by a domain name.
            :param str enabled:If set to true, then only domains that are enabled will be returned, if set to false only that are disabled will be returned. Any value other than 0, including no value, will be interpreted as true.
        """
        res = self.openstack_request(server_type='identity', server='domains', method='GET', filter=kwargs)
        return res

    def create_domain(self, **kwargs):
        """ Create the domain
        kwargs = {
            "domain": {
                "description": "Domain description",
                "enabled": True,
                "name": "myDomain"
            }
        }"""
        res = self.openstack_request(server_type='identity', server='domains', method='POST', body=kwargs)
        return res

    def update_domain(self, domain_id, *args, **kwargs):
        """Update the domain
        kwargs = {
            "domain": {
                "description": "Domain description",
                "enabled": True,
                "name": "myDomain"
            }
        }"""
        res = self.openstack_request(server_type='identity', server='domains/%s' % domain_id, method='PATCH',
                                     body=kwargs)
        return res

    def delete_domain(self, domain_id, *args, **kwargs):
        """Delete the domain"""
        res = self.openstack_request(server_type='identity', server='domains/%s' % domain_id, method='DELETE')

    def list_projects(self, *args, **kwargs):
        res = self.openstack_request(server_type='identity', server='projects', method='GET', filter=kwargs)
        return res

    def list_users(self, *args, **kwargs):
        res = self.openstack_request(server_type='identity', server='users', method='GET', filter=kwargs)
        return res

    def list_groups(self, *args, **kwargs):
        res = self.openstack_request(server_type='identity', server='groups', method='GET', filter=kwargs)
        return res

    def list_hypervisors(self,*args,**kwargs):
        res = self.openstack_request(server_type='compute', server='os-hypervisors', method='GET', filter=kwargs)
        if res.get('hypervisors'):
            return res.get('hypervisors')
    def show_hypervisors(self,id,*args,**kwargs):
        res = self.openstack_request(server_type='compute', server='os-hypervisors/%s'%id, method='GET', filter=kwargs)
        if res.get('hypervisor'):
            return res.get('hypervisor')
    def list_servers(self,*args,**kwargs):
        res = self.openstack_request(server_type='compute', server='servers', method='GET', filter=kwargs)
        if res.get('servers'):
            return res.get('servers')
    def show_server(self,id,*args,**kwargs):
        res = self.openstack_request(server_type='compute', server='servers/%s'%id, method='GET', filter=kwargs)
        if res.get('server'):
            return res.get('server')
    def list_flavor(self,*args,**kwargs):
        res = self.openstack_request(server_type='compute', server='flavors', method='GET', filter=kwargs)
        if res.get('flavors'):
            return res.get('flavors')
    def show_flavor(self,id,*args,**kwargs):
        res = self.openstack_request(server_type='compute', server='flavors/%s'%id, method='GET', filter=kwargs)
        if res.get('flavor'):
            return res.get('flavor')
    def migration_servers(self,host,server_id,*args,**kwargs):
        data={
            "migrate": {
                "host": host
            }
        }
        res = self.openstack_request(server_type='compute', server='servers/%s/action'%server_id, method='POST', body=data)
        print(res)