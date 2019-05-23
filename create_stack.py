#sample python code to create multiple cloudformation stacks
import boto3
import random

stack_list = []
num_stack = 50
user_str = 'bak-dc'
salt_flag = False
start_num = 0

#boto params
region_nm = 'us-west-2'

#CF params
domain_nm = 'dc.summit19labs.com.'
s3_url = 'https://s3-us-west-2.amazonaws.com/summit19-labs/dc/templates/dc-jira-dc.yaml'
j_ver = '8.1.0'
j_prod = 'Software'
j_dl_url = 'https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-8.1.0-EAP02-x64.bin'

for num in range(start_num,(num_stack+1)):
	if salt_flag: # if flag is present, add the salt to the instance name string
		salt = random.randrange(10,500,3)
		stack_name = user_str  + '-' + str(salt) + '-'
	else:
		stack_name = user_str + '-'
	stack_name = stack_name + str(num).zfill(3)
	stack_list.append(stack_name)

print ('List of stacks to be created:',stack_list)


client = boto3.client('cloudformation',region_name=region_nm)

while True:
	response = input('Press "P" to proceed or "C" to cancel:')
	if response == '' or response == 'C' or response == 'c':
		print ('Cancelling!!')
		break
	elif response == 'P' or response == 'p':
		print ('Creating Instances')
		for stack in stack_list:
			response = client.create_stack(
				StackName = stack,
				TemplateURL=s3_url,
				Parameters= [
				{'ParameterKey':'JiraProduct','ParameterValue':j_prod,'UsePreviousValue':False},
				{'ParameterKey':'JiraVersion','ParameterValue':j_ver,'UsePreviousValue':False},
				{'ParameterKey':'DeployEnvironment','ParameterValue':'prod','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeInstanceType','ParameterValue':'t3.large','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeMax','ParameterValue':'2','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeMin','ParameterValue':'2','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeVolumeSize','ParameterValue':'50','UsePreviousValue':False},
				{'ParameterKey':'DBInstanceClass','ParameterValue':'db.t2.medium','UsePreviousValue':False},
				{'ParameterKey':'DBIops','ParameterValue':'1000','UsePreviousValue':False},
				{'ParameterKey':'DBMasterUserPassword','ParameterValue':'Charlie101','UsePreviousValue':False},
				{'ParameterKey':'DBMultiAZ','ParameterValue':'false','UsePreviousValue':False},
				{'ParameterKey':'DBPassword','ParameterValue':'Charlie101','UsePreviousValue':False},
				{'ParameterKey':'DBStorage','ParameterValue':'200','UsePreviousValue':False},
				{'ParameterKey':'DBStorageEncrypted','ParameterValue':'false','UsePreviousValue':False},
				{'ParameterKey':'DBStorageType','ParameterValue':'General Purpose (SSD)','UsePreviousValue':False},
				{'ParameterKey':'AssociatePublicIpAddress','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'CidrBlock','ParameterValue':'0.0.0.0/0','UsePreviousValue':False},
				{'ParameterKey':'KeyPairName','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'SSLCertificateARN','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'CustomDnsName','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'HostedZone','ParameterValue':domain_nm,'UsePreviousValue':False},
				{'ParameterKey':'JiraDownloadUrl','ParameterValue':j_dl_url,'UsePreviousValue':False},
				{'ParameterKey':'LocalAnsibleGitRepo','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'LocalAnsibleGitSshKeyName','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'StartCollectd','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'TomcatContextPath','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'CatalinaOpts','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'JvmHeapOverride','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'DBPoolMaxSize','ParameterValue':'20','UsePreviousValue':False},
				{'ParameterKey':'DBPoolMinSize','ParameterValue':'20','UsePreviousValue':False},
				{'ParameterKey':'DBMaxIdle','ParameterValue':'20','UsePreviousValue':False},
				{'ParameterKey':'DBMaxWaitMillis','ParameterValue':'10000','UsePreviousValue':False},
				{'ParameterKey':'DBMinEvictableIdleTimeMillis','ParameterValue':'18000','UsePreviousValue':False},
				{'ParameterKey':'DBMinIdle','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'DBRemoveAbandoned','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'DBRemoveAbandonedTimeout','ParameterValue':'60','UsePreviousValue':False},
				{'ParameterKey':'DBTestOnBorrow','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'DBTestWhileIdle','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'DBTimeBetweenEvictionRunsMillis','ParameterValue':'60000','UsePreviousValue':False},
				{'ParameterKey':'MailEnabled','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'TomcatAcceptCount','ParameterValue':'10','UsePreviousValue':False},
				{'ParameterKey':'TomcatConnectionTimeout','ParameterValue':'20000','UsePreviousValue':False},
				{'ParameterKey':'TomcatDefaultConnectorPort','ParameterValue':'8080','UsePreviousValue':False},
				{'ParameterKey':'TomcatEnableLookups','ParameterValue':'false','UsePreviousValue':False},
				{'ParameterKey':'TomcatMaxThreads','ParameterValue':'200','UsePreviousValue':False},
				{'ParameterKey':'TomcatMinSpareThreads','ParameterValue':'10','UsePreviousValue':False},
				{'ParameterKey':'TomcatProtocol','ParameterValue':'HTTP/1.1','UsePreviousValue':False},
				{'ParameterKey':'TomcatRedirectPort','ParameterValue':'8443','UsePreviousValue':False},
				{'ParameterKey':'TomcatScheme','ParameterValue':'http','UsePreviousValue':False},
				],
    			OnFailure='ROLLBACK',
    		 	Capabilities=['CAPABILITY_IAM',],
    			Tags=[
    			{'Key': 'resource_owner','Value': 'csa_team'},
    			{'Key': 'Purpose','Value': 'dc_training_expo'},
    			{'Key': 'business_unit','Value': 'FieldOps'},
    			{'Key':'Name','Value':stack},
    			],
    			ClientRequestToken=str(random.randrange(10,1000,3)),
    			EnableTerminationProtection=False,
    			)
			if response['ResponseMetadata']['HTTPStatusCode'] == 200:
				print('Created Stack: %s' % stack)
	#print (response)'''
		exit()