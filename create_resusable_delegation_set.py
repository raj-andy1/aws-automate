#python script to create a reuseable delegation set

import boto3
import random
import json


client = boto3.client('route53')
'''
response = client.create_reusable_delegation_set(
    CallerReference=str(random.randrange(10,500,3)),
    HostedZoneId='Z3LTN44WAE5CAU')


'''

#response = client.list_reusable_delegation_sets()
response = client.get_reusable_delegation_set(
    Id='N1ANMKH3LHSTQ1'
)

print(response)

