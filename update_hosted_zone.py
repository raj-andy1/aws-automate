#python script to update parent domain with ns of child domain

import boto3
import json

#output of create_mul_hosted_zone.py with child domains and NS records
#hz_nm = {'user-004.charlieoil.com': ['ns-1844.awsdns-38.co.uk', 'ns-433.awsdns-54.com', 'ns-524.awsdns-01.net', 'ns-1440.awsdns-52.org'], 'user-006.charlieoil.com': ['ns-778.awsdns-33.net', 'ns-144.awsdns-18.com', 'ns-1205.awsdns-22.org', 'ns-1572.awsdns-04.co.uk'], 'user-008.charlieoil.com': ['ns-1529.awsdns-63.org', 'ns-125.awsdns-15.com', 'ns-2014.awsdns-59.co.uk', 'ns-913.awsdns-50.net'], 'user-009.charlieoil.com': ['ns-605.awsdns-11.net', 'ns-1783.awsdns-30.co.uk', 'ns-1159.awsdns-16.org', 'ns-66.awsdns-08.com'], 'user-010.charlieoil.com': ['ns-923.awsdns-51.net', 'ns-1744.awsdns-26.co.uk', 'ns-1443.awsdns-52.org', 'ns-441.awsdns-55.com']}
hz_nm = {'user-004.atlassian.camp': ['ns-1421.awsdns-49.org', 'ns-1830.awsdns-36.co.uk', 'ns-458.awsdns-57.com', 'ns-1012.awsdns-62.net'], 'user-006.atlassian.camp': ['ns-1048.awsdns-03.org', 'ns-1566.awsdns-03.co.uk', 'ns-230.awsdns-28.com', 'ns-843.awsdns-41.net'], 'user-008.atlassian.camp': ['ns-578.awsdns-08.net', 'ns-120.awsdns-15.com', 'ns-1506.awsdns-60.org', 'ns-1649.awsdns-14.co.uk'], 'user-009.atlassian.camp': ['ns-557.awsdns-05.net', 'ns-1983.awsdns-55.co.uk', 'ns-1510.awsdns-60.org', 'ns-469.awsdns-58.com'], 'user-010.atlassian.camp': ['ns-553.awsdns-05.net', 'ns-502.awsdns-62.com', 'ns-1595.awsdns-07.co.uk', 'ns-1095.awsdns-08.org']}
client = boto3.client('route53')

for hz in hz_nm:
    update_rr_response = client.change_resource_record_sets(
        HostedZoneId='Z1FT6JZ0OMF6YQ', #hosted zone id of the parent domain
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