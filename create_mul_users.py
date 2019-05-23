#sample python code to create users and attach it to groups on AWS using Boto3

import boto3
import random

num_users = 3 #provide the number of users
group_nm = {'j8dcd','opg','dc','j8'} #provide name of the group
user_list = dict.fromkeys(group_nm,[])
#print (user_list)
passwd='' #provide the password
salt_flag = False # Flag to set a random salt number to be added to the user name string to counter for aws delete user time lags

# if flag is present, add the salt to the username string, else do not add

for group in group_nm:
	for num in range(1,(num_users+1)):
		if salt_flag:
			salt = random.randrange(10,500,3)
			user_name = group  + '-' + str(salt) + '-user-'
		else:
			user_name = group +'-user-'
		user_name = user_name + str(num)
		user_list[group].append(user_name)
		

print ('List of users to be added is ', user_list)

'''
iam = boto3.client('iam')

for user_nm in user_list:
	user = iam.create_user(UserName=user_nm)
	group = iam.add_user_to_group(GroupName=group_nm,UserName=user_nm)
	iam.create_login_profile(UserName=user_nm,Password=passwd,PasswordResetRequired=False)
	print ('Created User: %s' % user['User']['UserName'])
	if group['ResponseMetadata']['HTTPStatusCode'] == 200:
		print ('User: %s has been added to group: %s' % (user['User']['UserName'],group_nm))
'''