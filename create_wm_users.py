#sample python code to create a list of users on AWS workmail using Boto3

import boto3
import random
import botocore.exceptions
import botocore

#Parameters
#user_list = ['admin','agrant','cowens','wsmith','jevans','mtaylor','kcampbell','eparis','rlee','hjennings','mdavis','rbaker'] #Empty user list that gets populated
user_list = ['admin']
passwd='AtlassianC0mp@ny' #provide the password
region_nm = 'us-west-2'
org_list = [{'org_id' : 'm-5d1189f97c3a4dec8b0beebda1f0f41d', 'domain_nm' : 'user-001.charlieoil.com', 'users':user_list},]
'''
{'org_id' : 'm-d4c045db4b57494cad152d007cbc0e15', 'domain_nm' : 'user-002.charlieoil.com', 'users': user_list},
{'org_id' : 'm-fb4ebffeb93347478d0ce290b15018e6', 'domain_nm' : 'user-003.charlieoil.com', 'users':user_list},
{'org_id' : 'm-1d820e9f64a4485ebbf6431a0e93e26c', 'domain_nm' : 'user-004.charlieoil.com', 'users':user_list},
{'org_id' : 'm-a9be2aba28204cbe9a0945c6ed37132d', 'domain_nm' : 'user-005.charlieoil.com', 'users':user_list},
{'org_id' : 'm-d3b36997d8724eb9854adf712b636aeb', 'domain_nm' : 'user-006.charlieoil.com', 'users':user_list},
{'org_id' : 'm-44ae0237ca4140c78bae4bb72da84a9e', 'domain_nm' : 'user-007.charlieoil.com', 'users':user_list},
{'org_id' : 'm-8488399331b844768a184d7dc24c577a', 'domain_nm' : 'user-008.charlieoil.com', 'users':user_list},
{'org_id' : 'm-0e11c6bdb17e4175980c0db9c631749a', 'domain_nm' : 'user-009.charlieoil.com', 'users':user_list},
{'org_id' : 'm-9e5065e8d58945db978e6101abca3603', 'domain_nm' : 'user-010.charlieoil.com', 'users':user_list}]'''


iam = boto3.client('workmail',region_name=region_nm) #provide region name since cloudtoken needs defaults to us-east-1

for org in org_list:
	#print (org['org_id']
	#print (domain)
	for usr in org['users']:
		print (usr)
		try:
			u = iam.create_user(OrganizationId=org['org_id'], Name=usr, DisplayName=usr, Password=passwd)
			print (u)
			ent_id = u['UserId']
		except botocore.exceptions.ClientError as err:
			#print (err.response)
			#print (err.response['Error']['Code'])
			if err.response['Error']['Code'] == 'NameAvailabilityException':
				print ('user name already exists')
			else:
				print (err.response['Error'])
				exit()
		finally:
			email = usr + '@' + org['domain_nm']
			print (email)
			try:
				r = iam.register_to_work_mail(OrganizationId=org['org_id'], EntityId=ent_id, Email=email)
				if r['ResponseMetadata']['HTTPStatusCode'] == 200:
					print ('Registered WorkMail User: %s with Email Id: %s' % (usr,email))
					exit()
			except botocore.exceptions.ClientError as err:
				print (err.response['Error'])
				exit()
	
	'''				
		if u['ResponseMetadata']['HTTPStatusCode'] == 200:
			print ('Created WorkMail User: %s' % usr)
			ent_id = u['UserId']
			email = usr + '@' + org['domain_nm']
			print (email)
			try:
				r = iam.register_to_work_mail(OrganizationId=org['org_id'], EntityId=ent_id, Email=email)
				if r['ResponseMetadata']['HTTPStatusCode'] == 200:
					print ('Registered WorkMail User: %s with Email Id: %s' % (usr,email))
					exit()
			except botocore.exceptions.ClientError as err:
				print (err.response['Error'])
				exit()	
'''		
