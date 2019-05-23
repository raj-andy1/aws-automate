#sample python code to delete a list of workmail users on AWS using Boto3

import boto3
import random

'''
num_users = 100 #provide the number of users
user_list = []
group_n = ''
group_nm = '' #provide name of the group
salt_flag = False # Flag to set a random salt number to be added to the user name string to counter for aws delete user time lags


for num in range(1,(num_users+1)):
	if salt_flag: # if flag is present, add the salt to the username string, else do not add
		salt = random.randrange(10,500,3)
		user_name = group_nm  + '-' + str(salt) + '-user-'
	else:
		user_name = group_nm +'user-'
	user_name = user_name + str(num).zfill(3)
	user_list.append(user_name)

print ('List of users to be deleted is ', user_list)
'''
user_id_list = []
user_id = {}
org_id = 'm-a613fdca685e4efdb6e748d916992864'

client = boto3.client('workmail')

nt = ''
iterM = 10
iterC = 0

while (iterC < iterM):
	iterC += 1
	if nt == '':
		response = client.list_users(
			OrganizationId = org_id,
			)
		#print ('****' + str(len(response['Users'])))
		for n in range(0,len(response['Users'])):
			key = response['Users'][n]['Name']
			user_id[key] = []
			user_id[key].extend([response['Users'][n]['State'],response['Users'][n]['Id']])
		if 'NextToken' in response:
			nt = response['NextToken']
			#print ('***' + nt)
		else:
			break
	else:
		response = client.list_users(
			OrganizationId = org_id,
			NextToken = nt,
			)
		#print ('+++' + str(len(response['Users'])))
		for n in range(0,len(response['Users'])):
			key = response['Users'][n]['Name']
			user_id[key] = []
			user_id[key].extend([response['Users'][n]['State'],response['Users'][n]['Id']])
		if 'NextToken' in response:
			nt = response['NextToken']
			#print ('+++' + nt)
		else:
			break

print (user_id)
#print (len(response['Users']))

'''
for n in range(0,100):
	key = response['Users'][n]['Name']
	user_id[key] = []
	user_id[key].extend([response['Users'][n]['State'],response['Users'][n]['Id']])
	if response['Users'][n]['State'] == 'ENABLED':
		user_id_list.append(response['Users'][n]['Id'])

print (user_id)
print (user_id_list)
#print (user_id_list)
#print (len(user_id_list))
'''
'''
for user in user_id_list:
	response = client.deregister_from_work_mail(
		OrganizationId = org_id,
		EntityId = user
		)
	print (response)
	response = client.delete_user(
		OrganizationId = org_id,
		UserId = user
		)
	print (response)
	'''



