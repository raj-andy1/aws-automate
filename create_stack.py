#sample python code to create multiple cloudformation stacks

'''
Instructions to create multiple stacks of Jira, Confluence or Bitbucket DC
1. Clone the repository aws-automate
2. Change the needed parameters for the stack you need to create on the appropriate files
	1. jira_stack_params.yaml for all jira DC stack
	2. confluence_stack_params.yaml for all confluence DC stack
	3. bitbucket_stack_params.yaml for all bitbucket DC stacks
3. authentication is not covered.
4. $ python3 create_stack.py bbdc for creating bitbucket DC stacks
5. $ python3 create_stack.py cnfdc for creating confluence DC stacks
6. $ python3 create_stack.py for creating jira DC stacks (default value is none provided is jdc)
7. Verify stack names and hit 'p' to proceed.
8. Logon to the AWS console and check the stack creation process
'''

import boto3
import random
import yaml
import sys

#parameters to create number of stacks
stack_list = []
num_stack = 2
salt_flag = True
start_num = 5

#boto params
region_nm = 'eu-central-1'

#stack parameters are loaded into a yaml file for easy readability and access

def get_template_url(template_type='jdc'):
	try:
		template_type = sys.argv[1]
	except IndexError:
		template_url = 'https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-jira/templates/quickstart-jira-dc.template.yaml'
		params_file = 'jira_stack_params.yaml'
	if template_type == 'bbdc': #bitbucket qs s3 url
		template_url = 'https://aws-quickstart.s3.amazonaws.com/quickstart-atlassian-bitbucket/templates/quickstart-bitbucket-dc.template.yaml'
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
		stack_name = user_str
	stack_name = stack_name + str(num).zfill(3)
	stack_list.append(stack_name)
print ('List of stacks to be created:',stack_list)

temp_url = get_template_url()[0]
stack_params = get_template_url()[1]

#print (temp_url)
#print (stack_params)

client = boto3.client('cloudformation',region_name=region_nm)


while True:
	response = input('Press "P" to proceed or "C" to cancel:')
	if response == '' or response == 'C' or response == 'c':
		print ('Cancelling!!')
		break
	elif response == 'P' or response == 'p':
		print ('Creating Instances')
		for stack in stack_list:
			try: 
				response = client.create_stack(
					StackName = stack,
					TemplateURL = temp_url,
					Parameters = stack_params,
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
				else:
					print (response)
			except Exception as e:
				print (e)
		exit()

