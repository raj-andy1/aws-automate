#python script to create multiple hosted zones

import boto3
import random
import json

num_hz = 20
hz_nm_list = []
domain_nm = 'charlieoil.com'

'''
creates hosted zones in the parent domain domain_nm of the form user-xxx.domain_nm, 
where xxx ranges from num_hz to num_hz+1
'''

for n in range(num_hz,(num_hz+1)):
	hz_nm_list.append('user-' + str(n).zfill(3) + '.' + domain_nm)

print(hz_nm_list)
hz_nm = dict.fromkeys(hz_nm_list,[]) #dict output to create a dict with key=name of hosted zone and value= NS records.
#print (hz_nm)


client = boto3.client('route53')

for hz in hz_nm_list:
	create_response = client.create_hosted_zone(
    Name=hz,
    CallerReference=str(random.randrange(10,5000)),
    HostedZoneConfig={
        'Comment': 'Test Zone for Enterprise Hybrid Migration Lab',
        'PrivateZone': False
    },
  )
	hz_nm[hz] = create_response['DelegationSet']['NameServers']
	print (create_response)

print (hz_nm) #output dict to be fed to update_hosted_zone.py
	

