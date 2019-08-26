#sample python code to create multiple cloudformation stacks

'''
Instructions to create multiple stacks of Jira, Confluence or Bitbucket DC
1. Clone the repository aws-automate


8. Logon to the AWS console and check the stack creation process
'''

import boto3
import random
import yaml
import sys

#parameters to create number of stacks
stack_list = []
num_stack = 2
salt_flag = False
start_num = 1

#boto params
region_nm = 'eu-central-1'

#stack parameters are loaded into a yaml file for easy readability and access

'''
stacks = {'jiradc11-latest-1':['https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-jira/templates/quickstart-jira-dc.template.yaml','jira_stack_latest_params.yaml'],
		'jiradc22-latest-2':['https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-jira/templates/quickstart-jira-dc.template.yaml','jira_stack_latest_params.yaml'],
		'jiradc33-er-1':['https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-jira/templates/quickstart-jira-dc.template.yaml','jira_stack_er_params.yaml'],
		'jiradc44-er-2':['https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-jira/templates/quickstart-jira-dc.template.yaml','jira_stack_er_params.yaml'],
		'cnfdc11-latest-1':['https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-confluence/templates/quickstart-confluence-master.template.yaml','confluence_stack_latest_params.yaml'],
		'cnfdc22-latest-2':['https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-confluence/templates/quickstart-confluence-master.template.yaml','confluence_stack_latest_params.yaml'],
		'cnfdc33-er-3':['https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-confluence/templates/quickstart-confluence-master.template.yaml','confluence_stack_er_params.yaml'],
		'cnfdc44-er-4':['https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-confluence/templates/quickstart-confluence-master.template.yaml','confluence_stack_er_params.yaml']}
'''
stacks = {
		'cnfdc11-latest-1':['https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-confluence/templates/quickstart-confluence-master.template.yaml','confluence_stack_latest_params.yaml'],
		'cnfdc22-latest-2':['https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-confluence/templates/quickstart-confluence-master.template.yaml','confluence_stack_latest_params.yaml'],
		'cnfdc33-er-3':['https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-confluence/templates/quickstart-confluence-master.template.yaml','confluence_stack_er_params.yaml'],
}

client = boto3.client('cloudformation',region_name=region_nm)


while True:
	response = input('Press "P" to proceed or "C" to cancel:')
	if response == '' or response == 'C' or response == 'c':
		print ('Cancelling!!')
		break
	elif response == 'P' or response == 'p':
		print ('Creating Instances')
		for k,v in stacks.items():
			stack = k
			temp_url, params_file = v
			stack_params = yaml.safe_load(open(params_file))
			#print ('stack_name:', stack)
			#print ('temp_url:', temp_url)
			#print ('stack_params:', stack_params)
			try: 
				response = client.create_stack(
					StackName = stack,
					TemplateURL = temp_url,
					Parameters = stack_params,
    				OnFailure='DO_NOTHING',
    		 		Capabilities=['CAPABILITY_IAM',],
    				Tags=[
    				{'Key': 'resource_owner','Value': 'arajagopalan'},
    				{'Key': 'service_name','Value': 'open-vienna-2019'},
    				{'Key': 'business_unit','Value': 'FieldOps'},
    				{'Key':'Name','Value':stack},
    				],
    				ClientRequestToken=str(random.randrange(10,1000,3)),
    				EnableTerminationProtection=False,
    				)
				if response['ResponseMetadata']['HTTPStatusCode'] == 200:
					print('Created Stack: %s' % stack)
				else:
					print (response)
			except Exception as e:
				print (e)
		exit()


'''
def get_template_url(template_type='jiradc'):
	try:
		template_type = sys.argv[1]
	except IndexError:
		template_url = 'https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-jira/templates/quickstart-jira-dc.template.yaml'
		params_file = 'jira_stack_params.yaml'
	if template_type == 'bbdc': #bitbucket qs s3 url
		#template_url = 'https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-bitbucket/templates/quickstart-bitbucket-dc.template.yaml'
		template_url = 'https://atl-andyr-cloudformation.s3.amazonaws.com/templates/quickstart-atlassian-bitbucket/templates/quickstart-bitbucket-dc.template.yaml'
		params_file = 'bitbucket_stack_params.yaml'
	elif template_type == 'cnfdc':  #confluence qs s3 url
		template_url = 'https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-confluence/templates/quickstart-confluence-master.template.yaml'
		params_file = 'confluence_stack_params.yaml'
	params = yaml.safe_load(open(params_file))
	
	return (template_url, params, template_type)

user_str = get_template_url()[2]

for num in range(start_num,(start_num+num_stack)):
	if salt_flag: # if flag is present, add the salt to the instance name string
		salt = random.randrange(10,500,3)
		stack_name = user_str + str(salt) + '-'
	else:
		stack_name = user_str + '-' + 'latest'
	stack_name = stack_name + str(num).zfill(1)
	stack_list.append(stack_name)


stack_list = ['bbdc-1']
print ('List of stacks to be created:',stack_list)

temp_url = get_template_url()[0]
stack_params = get_template_url()[1]

#print (temp_url)
#print (stack_params)
'''
