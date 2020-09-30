#sample python code to delete a list of workmail users on AWS using Boto3

import boto3
import random
import botocore
import botocore.exceptions

#Params
user_id = {}
org_id = 'm-5d1189f97c3a4dec8b0beebda1f0f41d'
region = 'us-west-2'

client = boto3.client('workmail',region_name=region)

nt = ''
iterM = 10
iterC = 0

while (iterC < iterM): #get the list of users for the organization with state and EntityID
	iterC += 1
	if nt == '':
		response = client.list_users(
			OrganizationId = org_id,
			)
		for n in range(0,len(response['Users'])):
			if response['Users'][n]['State'] == 'ENABLED':
				key = response['Users'][n]['Name']
				user_id[key] = []
				user_id[key] = response['Users'][n]['Id']
		if 'NextToken' in response:
			nt = response['NextToken']
		else:
			break
	else:
		response = client.list_users(
			OrganizationId = org_id,
			NextToken = nt,
			)
		for n in range(0,len(response['Users'])):
			if response['Users'][n]['State'] == 'ENABLED':
				key = response['Users'][n]['Name']
				user_id[key] = []
				user_id[key] = response['Users'][n]['Id']
		if 'NextToken' in response:
			nt = response['NextToken']
		else:
			break

#print (user_id)
for key,value in user_id.items():
	uname = key
	print (f'Deregistering user {uname} ')
	try:
		response = client.deregister_from_work_mail(
		OrganizationId = org_id,
		EntityId = value
		)
		if response['ResponseMetadata']['HTTPStatusCode'] == 200:
			print (f'Succesfully deregistered user {uname}')
	except botocore.exceptions.ClientError as err:
		print (err.response['Error'])
		continue
	print (f'Deleting user {uname}')
	try:
		response = client.delete_user(
		OrganizationId = org_id,
		UserId = value
		)
		if response['ResponseMetadata']['HTTPStatusCode'] == 200:
			print (f'Succesfully deleted user {uname}')
	except botocore.exceptions.ClientError as err:
		print (err.response['Error'])