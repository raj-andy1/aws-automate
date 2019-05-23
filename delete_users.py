#sample python code to delete a list of users on AWS using Boto3

import boto3
import random

num_users = 100 #provide the number of users
user_list = []
group_n = 'j8'
group_nm = 'j8' #provide name of the group
salt_flag = False # Flag to set a random salt number to be added to the user name string to counter for aws delete user time lags


for num in range(1,(num_users+1)):
	if salt_flag: # if flag is present, add the salt to the username string, else do not add
		salt = random.randrange(10,500,3)
		user_name = group_nm  + '-' + str(salt) + '-user-'
	else:
		user_name = group_nm +'-user-'
	user_name = user_name + str(num).zfill(3)
	user_list.append(user_name)

print ('List of users to be deleted is ', user_list)


iam = boto3.client('iam')

while True:
	response = input('Press "P" to proceed or "C" to cancel:')
	if response == '' or response == 'C' or response == 'c':
		print ('Cancelling!!')
		break
	elif response == 'P' or response == 'p':
		print ('Deleting users')
		for user_nm in user_list:
			user = iam.remove_user_from_group(GroupName=group_n,UserName=user_nm)
			#print (user)
			if user['ResponseMetadata']['HTTPStatusCode'] == 200:
				print ('Removed %s user from Group %s' % (user_nm,group_nm))
			user = iam.delete_login_profile(UserName=user_nm)
			#print (user)
			if user['ResponseMetadata']['HTTPStatusCode'] == 200:
				print ('Deleted Login Profile for %s user' % user_nm)
			user = iam.delete_user(UserName=user_nm)
			if user['ResponseMetadata']['HTTPStatusCode'] == 200:
				print ('Deleted User: %s' % user_nm)
			#print (user)
	exit()
