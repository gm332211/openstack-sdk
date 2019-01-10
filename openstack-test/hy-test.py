from sdk import Openstack
import time
op=Openstack.Openstack()
op.get_token()
while True:
    hyper_host = []
    move_hosts=[]
    destination_hosts=[]
    data=op.list_hypervisors()
    for hyper in data:
        if hyper.get('status'):
            if not hyper.get('id') in hyper_host:
                hyper_host.append({'id':hyper.get('id'),'name':hyper.get('hypervisor_hostname')})
    for host in hyper_host:
        host_data=op.show_hypervisors(host.get('id'))
        vcpus=host_data.get('vcpus',0)
        vcpus_used=host_data.get('vcpus_used',0)
        host['free_vcpus']=vcpus-vcpus_used
        if vcpus_used >=vcpus:
            move_hosts.append(host)
        else:
            destination_hosts.append(host)
    flag=True
    while flag:
        if move_hosts:
            print('Wait for the migration')
            if destination_hosts:
                print('Is the migration')
                for index,move_host in enumerate(move_hosts):
                    try:
                        destination_host=destination_hosts[0]
                        destination_hosts.pop(0)
                    except:
                        print('Insufficient migrated hosts')
                        flag = False
                    data=op.list_servers(host=move_host.get('name'))
                    try:
                        server_id=data[0].get('id')
                        server=op.show_server(server_id)
                        flavor_data = op.show_flavor(id=server['flavor']['id'])
                        server_vcpus=flavor_data['vcpus']
                        host=move_host.get('name')
                        if move_host.get('free_vcpus')>server_vcpus:
                            op.migration_servers(host=host,server_id=server_id)
                        move_hosts.pop(index)
                    except Exception as e:
                        print(e)
            else:
                print('There is no target host to migrate')
                flag = False
        else:
            print('There are no hosts to migrate')
            flag=False
    time.sleep(20)