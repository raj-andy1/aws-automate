#python script to update parent domain with ns of child domain

import boto3
import json

hz_ns = {'user-020.charlieoil.com': ['ns-302.awsdns-37.com', 'ns-1350.awsdns-40.org', 'ns-1819.awsdns-35.co.uk', 'ns-720.awsdns-26.net']}

client = boto3.client('route53')

for hz in hz_ns:
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
            {'Value': hz_ns[hz][0]},
            {'Value': hz_ns[hz][1]},
            {'Value': hz_ns[hz][2]},
            {'Value': hz_ns[hz][3]},
         ],}},]})
    print (update_rr_response)