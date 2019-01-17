#coding:utf-8
from sdk import Openstack
from test_config import setting as openstack_setting
import time
print('----自动迁移已开启----')
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
        host['vcpus'] = vcpus
        try:
            max_vcpus=vcpus*int(openstack_setting.threshold_vcpus)/100
        except:
            max_vcpus=vcpus
        if vcpus_used >=int(max_vcpus):
            move_hosts.append(host)
        else:
            destination_hosts.append(host)
    flag=True
    while flag:
        if move_hosts:
            if destination_hosts:
                print('等待迁移')
                for index,move_host in enumerate(move_hosts):
                    try:
                        destination_host=destination_hosts[0]
                        destination_hosts.pop(0)
                    except:
                        print('没有可迁移目标节点')
                        flag = False
                    data=op.list_servers(host=move_host.get('name'),status='ACTIVE')
                    try:
                        server_id=data[0].get('id')
                        server=op.show_server(server_id)
                        flavor_data = op.show_flavor(id=server['flavor']['id'])
                        server_vcpus=flavor_data['vcpus']
                        host=move_host.get('name')
                        try:
                            if int(move_host.get('free_vcpus'))+int(server_vcpus)<int(move_host.get('vcpus'))*int(openstack_setting.threshold_vcpus)/100:
                                print('正在迁移%s主机到%s节点'%(server_id,host))
                                op.migration_servers(host=host,server_id=server_id)
                                print('%s主机迁移成功' % server_id)
                        except:
                            print('%s主机迁移失败'%server_id)
                        move_hosts.pop(index)
                    except Exception as e:
                        print(e)
            else:
                print('没有可迁移目标节点')
                flag = False
        else:
            print('没有需要迁移的节点')
            flag=False
    wait_time=openstack_setting.wait_time
    time.sleep(int(wait_time))