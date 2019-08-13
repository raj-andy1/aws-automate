#sample python code to create multiple cloudformation stacks
import boto3
import random

stack_list = []
num_stack = 61
user_str = 'jira'
salt_flag = False
start_num = 2

#boto params
region_nm = 'eu-central-1'


for num in range(start_num,(num_stack+1)):
	if salt_flag: # if flag is present, add the salt to the instance name string
		salt = random.randrange(10,500,3)
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
				TemplateURL='https://open-hol-dc-on-aws.s3.eu-central-1.amazonaws.com/templates/quickstart-atlassian-jira/templates/quickstart-jira-dc.template.yaml',
				Parameters= [
				{'ParameterKey':'JiraProduct','ParameterValue':'Software','UsePreviousValue':False},
				{'ParameterKey':'JiraVersion','ParameterValue':'7.13.5','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeInstanceType','ParameterValue':'c5.xlarge','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeMax','ParameterValue':'1','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeMin','ParameterValue':'1','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeVolumeSize','ParameterValue':'50','UsePreviousValue':False},
				{'ParameterKey':'DBInstanceClass','ParameterValue':'db.m4.large','UsePreviousValue':False},
				{'ParameterKey':'DBIops','ParameterValue':'1000','UsePreviousValue':False},
				{'ParameterKey':'DBMasterUserPassword','ParameterValue':'Charlie101','UsePreviousValue':False},
				{'ParameterKey':'DBMultiAZ','ParameterValue':'false','UsePreviousValue':False},
				{'ParameterKey':'DBPassword','ParameterValue':'Charlie101','UsePreviousValue':False},
				{'ParameterKey':'DBStorage','ParameterValue':'200','UsePreviousValue':False},
				{'ParameterKey':'DBStorageEncrypted','ParameterValue':'false','UsePreviousValue':False},
				{'ParameterKey':'DBStorageType','ParameterValue':'General Purpose (SSD)','UsePreviousValue':False},
				{'ParameterKey':'InternetFacingLoadBalancer','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'CidrBlock','ParameterValue':'0.0.0.0/0','UsePreviousValue':False},
				{'ParameterKey':'KeyPairName','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'SSLCertificateARN','ParameterValue':'arn:aws:acm:eu-central-1:755021131661:certificate/424eb0f8-24bd-4a1c-96db-028eccab1bf9','UsePreviousValue':False},
				{'ParameterKey':'CustomDnsName','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'HostedZone','ParameterValue':'open.atlassian.guru.','UsePreviousValue':False},
				{'ParameterKey':'DeploymentAutomationRepository','ParameterValue':'https://bitbucket.org/atlassian/dc-deployments-automation.git','UsePreviousValue':False},
				{'ParameterKey':'DeploymentAutomationBranch','ParameterValue':'master','UsePreviousValue':False},
				{'ParameterKey':'DeploymentAutomationPlaybook','ParameterValue':'aws_jira_dc_node.yml','UsePreviousValue':False},
				{'ParameterKey':'DeploymentAutomationKeyName','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'TomcatContextPath','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'CatalinaOpts','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'JvmHeapOverride','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'DBPoolMaxSize','ParameterValue':'20','UsePreviousValue':False},
				{'ParameterKey':'DBPoolMinSize','ParameterValue':'20','UsePreviousValue':False},
				{'ParameterKey':'DBMaxIdle','ParameterValue':'20','UsePreviousValue':False},
				{'ParameterKey':'DBMaxWaitMillis','ParameterValue':'10000','UsePreviousValue':False},
				{'ParameterKey':'DBMinEvictableIdleTimeMillis','ParameterValue':'18000','UsePreviousValue':False},
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
				{'ParameterKey':'TomcatScheme','ParameterValue':'https','UsePreviousValue':False},
				],
    			OnFailure='DO_NOTHING',
    		 	Capabilities=['CAPABILITY_IAM',],
    			Tags=[
    			{'Key': 'resource_owner','Value': 'andyr'},
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