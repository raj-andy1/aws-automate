#sample python code to delete cloudformation stacks
import boto3


stack_list = ['jiradc11-latest-1','jiradc22-latest-2','jiradc33-er-3','jiradc44-er-4','cnfdc11-latest-1','cnfdc22-latest-2','cnfdc33-er-3','cnfdc44-er-4','bbdc-1','bbdc-2']

client = boto3.client('cloudformation',region_name='us-east-1')

for stack in stack_list:
	response = client.delete_stack(
		StackName = stack,
		)
	print ('Deleting stack with name %s' % stack)
	print (response)