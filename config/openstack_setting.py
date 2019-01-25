DOMAIN='default'
PROJECT='admin'
USERNAME='admin'
PASSWORD='password'
openstack_endpoint={
    'identity':{
        'url': 'http://192.168.1.10/identity',
        'version': 3
    },
    'compute':{
        'url': 'http://192.168.1.10/compute',
        'version': 2
    },
    'image': {
        'url': 'http://192.168.1.10/image',
        'version': 2
    },
    'network': {
        'url': 'http://192.168.1.10:9696',
        'version': 2
    }
}