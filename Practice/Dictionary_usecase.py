ec2_instance_info = [
    {
        'instance_name': 'app_server',
        'instance_type': 't2.micro'
    },
    {
        'instance_name': 'app_server_02',
        'instance_type': 't2.medium'
    },
    {
        'instance_name': 'DataBase_server',
        'instance_type': 't2.large'
    }
]

print(ec2_instance_info[2]['instance_name'])
# [] you spesify posisition of the item you want to print
# This will print 'DataBase_server' because I asked for instance_name