#python script to update parent domain with ns of child domain

import boto3
import json

#output of create_mul_hosted_zone.py with child domains and NS records
hz_nm = {'user-020.charlieoil.com': ['ns-302.awsdns-37.com', 'ns-1350.awsdns-40.org', 'ns-1819.awsdns-35.co.uk', 'ns-720.awsdns-26.net']}

client = boto3.client('route53')

for hz in hz_nm:
    update_rr_response = client.change_resource_record_sets(
        HostedZoneId='Z3LTN44WAE5CAU', #hosted zone id of the parent domain
	   ChangeBatch={
	   'Changes': [{
	   'Action': 'CREATE',
        'ResourceRecordSet': {
        'Name': hz,
        'Type': 'NS',
        'TTL': 60,
        'ResourceRecords': [
            {'Value': hz_nm[hz][0]},
            {'Value': hz_nm[hz][1]},
            {'Value': hz_nm[hz][2]},
            {'Value': hz_nm[hz][3]},
         ],}},]})
    print (update_rr_response)