#sample python code to create multiple cloudformation stacks
import boto3
import random

stack_list = []
num_stack = 17
user_str = 'jira-backup-west'
salt_flag = False
start_num = 2

#boto params
region_nm = 'us-west-2'


for num in range(start_num,(num_stack+1)):
	if salt_flag: # if flag is present, add the salt to the instance name string
		salt = random.randrange(100,500,3)
		stack_name = user_str + '-' + str(salt) + '-'
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
				TemplateURL='https://atl-events.s3.amazonaws.com/templates/jira-quickstart.yaml',
				Parameters= [
				{'ParameterKey':'JiraProduct','ParameterValue':'Software','UsePreviousValue':False},
				{'ParameterKey':'JiraVersion','ParameterValue':'8.12.1','UsePreviousValue':False},
				{'ParameterKey':'CloudWatchIntegration','ParameterValue':'Metrics and Logs','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeInstanceType','ParameterValue':'c5.xlarge','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeMax','ParameterValue':'1','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeMin','ParameterValue':'1','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeVolumeSize','ParameterValue':'50','UsePreviousValue':False},
				{'ParameterKey':'DeploymentAutomationRepository','ParameterValue':'https://bitbucket.org/atlassian/dc-deployments-automation.git','UsePreviousValue':False},
				{'ParameterKey':'DeploymentAutomationBranch','ParameterValue':'master','UsePreviousValue':False},
				{'ParameterKey':'DeploymentAutomationPlaybook','ParameterValue':'aws_jira_dc_node.yml','UsePreviousValue':False},
				{'ParameterKey':'DeploymentAutomationCustomParams','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'DeploymentAutomationKeyName','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'DBEngine','ParameterValue':'PostgreSQL','UsePreviousValue':False},
				{'ParameterKey':'DBEngineVersion','ParameterValue':'9','UsePreviousValue':False},
				{'ParameterKey':'DBInstanceClass','ParameterValue':'db.m5.large','UsePreviousValue':False},
				{'ParameterKey':'DBIops','ParameterValue':'1000','UsePreviousValue':False},
				{'ParameterKey':'DBMasterUserPassword','ParameterValue':'Test#1234','UsePreviousValue':False},
				{'ParameterKey':'DBMultiAZ','ParameterValue':'false','UsePreviousValue':False},
				{'ParameterKey':'DBPassword','ParameterValue':'Test#1234','UsePreviousValue':False},
				{'ParameterKey':'DBStorage','ParameterValue':'200','UsePreviousValue':False},
				{'ParameterKey':'DBStorageEncrypted','ParameterValue':'false','UsePreviousValue':False},
				{'ParameterKey':'DBStorageType','ParameterValue':'General Purpose (SSD)','UsePreviousValue':False},
				{'ParameterKey':'BastionHostRequired','ParameterValue':'false','UsePreviousValue':False},
				{'ParameterKey':'KeyPairName','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'InternetFacingLoadBalancer','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'CidrBlock','ParameterValue':'0.0.0.0/0','UsePreviousValue':False},
				{'ParameterKey':'SSLCertificateARN','ParameterValue':'arn:aws:acm:us-west-2:948417468652:certificate/6a8ad93d-f2d4-49ae-a4d5-d4c7db8146f9','UsePreviousValue':False},
				{'ParameterKey':'CustomDnsName','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'HostedZone','ParameterValue':'pe.atlassian.camp.','UsePreviousValue':False},
				{'ParameterKey':'TomcatContextPath','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'CatalinaOpts','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'JvmHeapOverride','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'DBPoolMaxSize','ParameterValue':'20','UsePreviousValue':False},
				{'ParameterKey':'DBPoolMinSize','ParameterValue':'20','UsePreviousValue':False},
				{'ParameterKey':'DBMaxIdle','ParameterValue':'20','UsePreviousValue':False},
				{'ParameterKey':'DBMaxWaitMillis','ParameterValue':'10000','UsePreviousValue':False},
				{'ParameterKey':'DBMinEvictableIdleTimeMillis','ParameterValue':'180000','UsePreviousValue':False},
				{'ParameterKey':'DBMinIdle','ParameterValue':'10','UsePreviousValue':False},
				{'ParameterKey':'DBRemoveAbandoned','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'DBRemoveAbandonedTimeout','ParameterValue':'60','UsePreviousValue':False},
				{'ParameterKey':'DBTestOnBorrow','ParameterValue':'false','UsePreviousValue':False},
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
				{'ParameterKey':'QSS3BucketName','ParameterValue':'aws-quickstart','UsePreviousValue':False},
				{'ParameterKey':'QSS3KeyPrefix','ParameterValue':'quickstart-atlassian-jira/','UsePreviousValue':False},
				{'ParameterKey':'ExportPrefix','ParameterValue':'ATL-','UsePreviousValue':False},
				],
    			OnFailure='DO_NOTHING',
    		 	Capabilities=['CAPABILITY_IAM',],
    			Tags=[
    			{'Key': 'resource_owner','Value': 'mchandira'},
    			{'Key': 'Purpose','Value': 'jira-testing'},
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