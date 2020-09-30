#sample python code to delete cloudformation stacks
import boto3

stack_list = ['jira-201', 'jira-202', 'jira-203', 'jira-204', 'jira-205', 'jira-206', 'jira-207', 'jira-208', 'jira-209', 'jira-210', 'jira-211', 'jira-212', 'jira-213', 'jira-214', 'jira-215', 'jira-216', 'jira-217', 'jira-218', 'jira-219', 'jira-220', 'jira-221', 'jira-222', 'jira-223', 'jira-224', 'jira-225', 'jira-226', 'jira-227', 'jira-228', 'jira-229', 'jira-230', 'jira-231', 'jira-232', 'jira-233', 'jira-234', 'jira-235', 'jira-236', 'jira-237', 'jira-238', 'jira-239', 'jira-240', 'jira-241', 'jira-242', 'jira-243', 'jira-244', 'jira-245', 'jira-246', 'jira-247', 'jira-248', 'jira-249', 'jira-250', 'jira-251', 'jira-252', 'jira-253', 'jira-254', 'jira-255', 'jira-256', 'jira-257', 'jira-258', 'jira-259', 'jira-260', 'jira-261', 'jira-262', 'jira-263', 'jira-264', 'jira-265', 'jira-266', 'jira-267', 'jira-268', 'jira-269', 'jira-270', 'jira-271', 'jira-272', 'jira-273', 'jira-274', 'jira-275', 'jira-276', 'jira-277', 'jira-278', 'jira-279', 'jira-280']
client = boto3.client('cloudformation',region_name='us-west-2')

for stack in stack_list:
	response = client.delete_stack(
		StackName = stack,
		)
	print ('Deleting stack with name %s' % stack)
	print (response)