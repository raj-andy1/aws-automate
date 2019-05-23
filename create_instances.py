#python script to create n instances from ami 

import boto3
import random
import json
import time

#program parameters
num_instances = 200
instance_list=[]
user_str = 'jsd'
domain_nm = 'og.summit19labs.com'
salt_flag = False #Flag set to add a random number to instance name string to counter for AWS instance delete time lag
start_num = 0

#boto3 parameters
region_nm = 'us-west-2'

#ec2 instance parameters
dry_run = False #whether to do a dry run to validate parameters
iam_arn= 'arn:aws:iam::729545084641:instance-profile/ec2_ssm_role_for_og' #arn for the instance profile to be attached to the instance during creation
if_del_on_term = True #Wheter the resource should be deleted when the instance is deleted
if_enc = False #if encryption required
if_public_ip = True #Whether public IP should be assigned
img_id = 'ami-0077910e4c35b2a3c' #ami id of the image to be deployed
inst_type = 'm5.large'  #instance type
key_nm = 'atl-master-us-west-2' #SSH Key Name, key needs to be uploaded first
sec_g = ['sg-0f9dc38a01de01cb9'] #security group list
snet_id = 'subnet-0f463f0d9bb2d4b94' #subnet Id
vol_sz = 100 #size of volume
vol_type = 'gp2' #type of volume



for num in range(start_num,(num_instances+1)):
	if salt_flag: # if flag is present, add the salt to the instance name string
		salt = random.randrange(10,500,3)
		instance_name = user_str  + '-' + str(salt) +'-'
	else:
		instance_name = user_str + '-'
	instance_name = instance_name + str(num).zfill(3) + '.' + domain_nm
	instance_list.append(instance_name)

print('List of instances:', instance_list)

ec2 = boto3.resource('ec2',region_name=region_nm)

while True:
	response = input('Press "P" to proceed or "C" to cancel:')
	if response == '' or response == 'C' or response == 'c':
		print ('Cancelling!!')
		break
	elif response == 'P' or response == 'p':
		print ('Creating Instances')
		for inst_nm in instance_list:
			instance = ec2.create_instances(
				DryRun=dry_run,
				ImageId = img_id,
				MinCount =1,
				MaxCount = 1,
				InstanceType = inst_type,
				KeyName = key_nm,
				IamInstanceProfile={
					'Arn':iam_arn,
				},
				NetworkInterfaces=[
				{
					'DeviceIndex':0,
					'AssociatePublicIpAddress': if_public_ip,
					'DeleteOnTermination': if_del_on_term,
					'SubnetId':snet_id,
					'Groups': sec_g,
				}],
				BlockDeviceMappings=[
				{ 
				'DeviceName':'/dev/xvda',
				'Ebs': {
					'DeleteOnTermination':if_del_on_term,
					'VolumeSize': vol_sz,
					'VolumeType':vol_type,
					'Encrypted': if_enc,
				},
				}],
				TagSpecifications=[
				{
				'ResourceType': 'instance',
				'Tags': [
				{
                    'Key': 'Name',
                    'Value': inst_nm,
                },]},],
				)
			#print (instance)
			print ('Created Instance:',instance[0].instance_id)
			inst = boto3.client('ec2',region_name=region_nm)
			time.sleep(5)
			inst_desc = inst.describe_instances(
				DryRun = dry_run,
				InstanceIds=[instance[0].instance_id,],
				)
			#print ('Instance Description***')
			#print (inst_desc)
			inst_pub_ip = inst_desc['Reservations'][0]['Instances'][0]['PublicIpAddress']
			print ('PublicIpAddress***')
			print (inst_pub_ip)
			dns = boto3.client('route53')
			gethz = dns.list_hosted_zones_by_name(
				DNSName = domain_nm,
				)
			#print (gethz)
			rrupdate = dns.change_resource_record_sets(
			HostedZoneId=gethz['HostedZones'][0]['Id'][12:],
			ChangeBatch={
			'Changes': [
			{
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': inst_nm,
                    'Type': 'A',
                    'TTL': 300,
                    'ResourceRecords': [
                        {
                            'Value': inst_pub_ip
                        },
                    ],}},]})
			print ('R53 Update status')
			#print (rrupdate)
			if rrupdate['ResponseMetadata']['HTTPStatusCode'] == 200:
				print ('Added instance %s with public ip %s to Route53 and status is %s' %(inst_nm, inst_pub_ip,rrupdate['ChangeInfo']['Status']))
			time.sleep(5)
		exit()

		
