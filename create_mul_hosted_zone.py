#python script to create multiple hosted zones

import boto3
import random
import json

num_hz = 1
hz_nm_list = []
domain_nm = 'charlieoil.com'
delegation_set_id = 'N1ANMKH3LHSTQ1'

for n in range(num_hz,(num_hz+1)):
	hz_nm_list.append('user-' + str(n).zfill(3) + '.' + domain_nm)

print(hz_nm_list)

client = boto3.client('route53')

for hz in hz_nm_list:
	create_response = client.create_hosted_zone(
    Name=hz,
    CallerReference=str(random.randrange(10,500,3)),
    HostedZoneConfig={
        'Comment': 'Test Zone for Enterprise Hybrid Migration Lab',
        'PrivateZone': False
    },
  )
	print (create_response)
	ns_str = ''
	for ns in create_response['DelegationSet']['NameServers']:
		ns_str += ns + ';' + '\n'
	print (ns_str)
	update_rr_response = client.change_resource_record_sets(
		HostedZoneId='Z3LTN44WAE5CAU',
		ChangeBatch={
		'Changes': [{
		'Action': 'CREATE',
        'ResourceRecordSet': {
        'Name': hz,
        'Type': 'NS',
        'TTL': 60,
        'ResourceRecords': [
        {
        'Value': ns_str
		},],}},]})
	print (update_rr_response)


