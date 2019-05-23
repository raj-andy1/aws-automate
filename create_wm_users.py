#sample python code to create a list of users on AWS workmail using Boto3

import boto3
import random

#Parameters
num_users = 200 #provide the number of users
user_list = [] #Empty user list that gets populated
group_nm = '' #provide name of the group
passwd='AtlassianSummit19L@b' #provide the password
org_id = 'm-a613fdca685e4efdb6e748d916992864' #workmail organization ID
domain_nm = 'atlassian.guru'
region_nm = 'us-east-1'
salt_flag = False # Flag to set a random salt number to be added to the user name string to counter for aws delete user time lags


for num in range(1,(num_users+1)):
	if salt_flag: # if flag is present, add the salt to the username string, else do not add
		salt = random.randrange(10,500,3)
		user_name = group_nm  + '-' + str(salt) + '-user-'
	else:
		user_name = group_nm +'user-'
	user_name = user_name + str(num).zfill(3)
	user_list.append(user_name)

print ('List of users to be added is ', user_list)

iam = boto3.client('workmail',region_name=region_nm) #provide region name since cloudtoken needs defaults to us-east-1

while True:
	response = input('Press "P" to proceed or "C" to cancel:')
	if response == '' or response == 'C' or response == 'c':
		print ('Cancelling!!')
		break
	elif response == 'P' or response == 'p':
		print ('Creating users')
		for user_nm in user_list:
			user = iam.create_user(OrganizationId=org_id,Name=user_nm, \
				DisplayName=user_nm,Password=passwd)
			#print (user)
			if user['ResponseMetadata']['HTTPStatusCode'] == 200:
				print ('Created WorkMail User: %s' % user_nm)
			ent_id = user['UserId']
			email_id = user_nm + '@' + domain_nm
			#print (email_id)
			user = iam.register_to_work_mail(OrganizationId=org_id,EntityId=ent_id,\
				Email=email_id)
			if user['ResponseMetadata']['HTTPStatusCode'] == 200:
				print ('Registered WorkMail User: %s with Email Id: %s' % (user_nm,email_id))
		exit()