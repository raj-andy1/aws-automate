#sample python code to create a list of users on AWS workmail using Boto3

import boto3
import random
import botocore
import botocore.exceptions


#Parameters
user_list = ['admin','agrant','cowens','wsmith','jevans','mtaylor','kcampbell','eparis','rlee','hjennings','mdavis','rbaker']
passwd='AtlassianC0mp@ny' #provide the password
region_nm = 'us-west-2'
org_list = [{'org_id' : 'm-5d1189f97c3a4dec8b0beebda1f0f41d', 'domain_nm' : 'user-001.charlieoil.com', 'users':user_list},
{'org_id' : 'm-d4c045db4b57494cad152d007cbc0e15', 'domain_nm' : 'user-002.charlieoil.com', 'users': user_list},
{'org_id' : 'm-fb4ebffeb93347478d0ce290b15018e6', 'domain_nm' : 'user-003.charlieoil.com', 'users':user_list},
{'org_id' : 'm-1d820e9f64a4485ebbf6431a0e93e26c', 'domain_nm' : 'user-004.charlieoil.com', 'users':user_list},
{'org_id' : 'm-a9be2aba28204cbe9a0945c6ed37132d', 'domain_nm' : 'user-005.charlieoil.com', 'users':user_list},
{'org_id' : 'm-d3b36997d8724eb9854adf712b636aeb', 'domain_nm' : 'user-006.charlieoil.com', 'users':user_list},
{'org_id' : 'm-44ae0237ca4140c78bae4bb72da84a9e', 'domain_nm' : 'user-007.charlieoil.com', 'users':user_list},
{'org_id' : 'm-8488399331b844768a184d7dc24c577a', 'domain_nm' : 'user-008.charlieoil.com', 'users':user_list},
{'org_id' : 'm-0e11c6bdb17e4175980c0db9c631749a', 'domain_nm' : 'user-009.charlieoil.com', 'users':user_list},
{'org_id' : 'm-9e5065e8d58945db978e6101abca3603', 'domain_nm' : 'user-010.charlieoil.com', 'users':user_list}]


iam = boto3.client('workmail',region_name=region_nm) #provide region name since cloudtoken needs defaults to us-east-1

for org in org_list:
	for usr in org['users']:
		ent_id = ''
		try:
			print (f'Creating WorkMail User:{usr}')
			u = iam.create_user(OrganizationId=org['org_id'], Name=usr, DisplayName=usr, Password=passwd) #create the user
			ent_id = u['UserId']
			if u['ResponseMetadata']['HTTPStatusCode'] == 200:
				print (f'Successfully created WorkMail User:{usr}')
		except botocore.exceptions.ClientError as err:
			if err.response['Error']['Code'] == 'NameAvailabilityException':
				print (f'User name "{usr}" already exists')
				n = iam.list_users(OrganizationId=org['org_id'], MaxResults=15) #get entity id of existing user if exception is thrown
				for usrs in n['Users']:
					uid = usrs['Id']
					uname = usrs['Name']
					state = usrs['State']
					if (uname == 'admin' and state == 'ENABLED'):
						ent_id = uid
				#print (ent_id)
			else:
				print (err.response['Error'])
				exit()
		finally: #register emailID for user and enable the user
			email = usr + '@' + org['domain_nm']
			if ent_id != '':
				try:
					print (f'Registering WorkMail User "{usr}" with Email Id "{email}"')
					r = iam.register_to_work_mail(OrganizationId=org['org_id'], EntityId=ent_id, Email=email)
					if r['ResponseMetadata']['HTTPStatusCode'] == 200:
						print (f'Sucessfully registered WorkMail User "{usr}" with Email Id "{email}"')
				except botocore.exceptions.ClientError as err:
					print (err.response['Error'])
