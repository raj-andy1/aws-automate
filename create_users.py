#sample python code to create a list of users on AWS using Boto3

import boto3
import random

#Parameters
num_users = 10 #provide the number of users
user_list = []
group_nm = 'jiraevent' #provide name of the group
passwd='AtlassianSummit20L@b' #provide the password
salt_flag = False # Flag to set a random salt number to be added to the user name string to counter for aws delete user time lags


for num in range(1,(num_users+1)):
	if salt_flag: # if flag is present, add the salt to the username string, else do not add
		salt = random.randrange(10,500,3)
		user_name = str(salt) + 'user-'
	else:
		user_name = 'user-'
	user_name = user_name + str(num).zfill(3)
	user_list.append(user_name)

print ('List of users to be added is ', user_list)

iam = boto3.client('iam')

try:
	for groupname in [i["GroupName"] for i in list(iam.list_groups().values())[0]]:
		if group_nm not in groupname:
			break
		else:
			pass
	iam.create_group(GroupName=group_nm)
except Exception as e:
	print("Group present")
	pass

try:
	while True:
		response = input('Press "P" to proceed or "C" to cancel:')
		if response == '' or response == 'C' or response == 'c':
			print ('Cancelling!!')
			break
		elif response == 'P' or response == 'p':
			for user_nm in user_list:
				user = iam.create_user(UserName=user_nm)
				group = iam.add_user_to_group(GroupName=group_nm,UserName=user_nm)
				iam.create_login_profile(UserName=user_nm,Password=passwd,PasswordResetRequired=False)
				print ('Created User: %s' % user['User']['UserName'])
				if group['ResponseMetadata']['HTTPStatusCode'] == 200:
					print ('User: %s has been added to group: %s' % (user['User']['UserName'],group_nm))
			exit()
except iam.exceptions.EntityAlreadyExistsException:
	print ('Users present')
	pass
