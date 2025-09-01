ec2_instance_1 = {
    'instance_name' : 'app_server',
    'instance_type' : 't2.micro',
    'ami_id' : 'ami-12345678',
}


ec2_instance_2 = {
    'instance_name' : 'app_server_2',
    'instance_type' : 't2.micro',
    'ami_id' : 'ami-1234534239',
}

ec2_instance_3 = {
    'instance_name' : 'db_server',
    'instance_type' : 't2.medium',
    'ami_id' : 'ami-1234e3493dgf',
}

print (ec2_instance_3.get('instance_type'))  # This will print 'app_server_2'