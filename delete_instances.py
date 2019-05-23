#python script to delete instances from a given list of instances

import boto3
import random
import json
import time
from botocore.exceptions import ClientError

instance_list=['jsd-005.og.summit19labs.com', 'jsd-006.og.summit19labs.com', 'jsd-007.og.summit19labs.com', 'jsd-008.og.summit19labs.com', 'jsd-009.og.summit19labs.com', 'jsd-010.og.summit19labs.com', 'jsd-011.og.summit19labs.com', 'jsd-012.og.summit19labs.com', 'jsd-013.og.summit19labs.com', 'jsd-014.og.summit19labs.com', 'jsd-015.og.summit19labs.com', 'jsd-016.og.summit19labs.com', 'jsd-017.og.summit19labs.com', 'jsd-018.og.summit19labs.com', 'jsd-019.og.summit19labs.com', 'jsd-020.og.summit19labs.com', 'jsd-021.og.summit19labs.com', 'jsd-022.og.summit19labs.com', 'jsd-023.og.summit19labs.com', 'jsd-024.og.summit19labs.com', 'jsd-025.og.summit19labs.com', 'jsd-026.og.summit19labs.com', 'jsd-027.og.summit19labs.com', 'jsd-028.og.summit19labs.com', 'jsd-029.og.summit19labs.com', 'jsd-030.og.summit19labs.com', 'jsd-031.og.summit19labs.com', 'jsd-032.og.summit19labs.com', 'jsd-033.og.summit19labs.com', 'jsd-034.og.summit19labs.com', 'jsd-035.og.summit19labs.com', 'jsd-036.og.summit19labs.com', 'jsd-037.og.summit19labs.com', 'jsd-038.og.summit19labs.com', 'jsd-039.og.summit19labs.com', 'jsd-040.og.summit19labs.com', 'jsd-041.og.summit19labs.com', 'jsd-042.og.summit19labs.com', 'jsd-043.og.summit19labs.com', 'jsd-044.og.summit19labs.com', 'jsd-045.og.summit19labs.com', 'jsd-046.og.summit19labs.com', 'jsd-047.og.summit19labs.com', 'jsd-048.og.summit19labs.com', 'jsd-049.og.summit19labs.com', 'jsd-050.og.summit19labs.com', 'jsd-051.og.summit19labs.com', 'jsd-052.og.summit19labs.com', 'jsd-053.og.summit19labs.com', 'jsd-054.og.summit19labs.com', 'jsd-055.og.summit19labs.com', 'jsd-056.og.summit19labs.com', 'jsd-057.og.summit19labs.com', 'jsd-058.og.summit19labs.com', 'jsd-059.og.summit19labs.com', 'jsd-060.og.summit19labs.com', 'jsd-061.og.summit19labs.com', 'jsd-062.og.summit19labs.com', 'jsd-063.og.summit19labs.com', 'jsd-064.og.summit19labs.com', 'jsd-065.og.summit19labs.com', 'jsd-066.og.summit19labs.com', 'jsd-067.og.summit19labs.com', 'jsd-068.og.summit19labs.com', 'jsd-069.og.summit19labs.com', 'jsd-070.og.summit19labs.com', 'jsd-071.og.summit19labs.com', 'jsd-072.og.summit19labs.com', 'jsd-073.og.summit19labs.com', 'jsd-074.og.summit19labs.com', 'jsd-075.og.summit19labs.com', 'jsd-076.og.summit19labs.com', 'jsd-077.og.summit19labs.com', 'jsd-078.og.summit19labs.com', 'jsd-079.og.summit19labs.com', 'jsd-080.og.summit19labs.com', 'jsd-081.og.summit19labs.com', 'jsd-082.og.summit19labs.com', 'jsd-083.og.summit19labs.com', 'jsd-084.og.summit19labs.com', 'jsd-085.og.summit19labs.com', 'jsd-086.og.summit19labs.com', 'jsd-087.og.summit19labs.com', 'jsd-088.og.summit19labs.com', 'jsd-089.og.summit19labs.com', 'jsd-090.og.summit19labs.com', 'jsd-091.og.summit19labs.com', 'jsd-092.og.summit19labs.com', 'jsd-093.og.summit19labs.com', 'jsd-094.og.summit19labs.com', 'jsd-095.og.summit19labs.com', 'jsd-096.og.summit19labs.com', 'jsd-097.og.summit19labs.com', 'jsd-098.og.summit19labs.com', 'jsd-099.og.summit19labs.com', 'jsd-100.og.summit19labs.com', 'jsd-101.og.summit19labs.com', 'jsd-102.og.summit19labs.com', 'jsd-103.og.summit19labs.com', 'jsd-104.og.summit19labs.com', 'jsd-105.og.summit19labs.com', 'jsd-106.og.summit19labs.com', 'jsd-107.og.summit19labs.com', 'jsd-108.og.summit19labs.com', 'jsd-109.og.summit19labs.com', 'jsd-110.og.summit19labs.com', 'jsd-111.og.summit19labs.com', 'jsd-112.og.summit19labs.com', 'jsd-113.og.summit19labs.com', 'jsd-114.og.summit19labs.com', 'jsd-115.og.summit19labs.com', 'jsd-116.og.summit19labs.com', 'jsd-117.og.summit19labs.com', 'jsd-118.og.summit19labs.com', 'jsd-119.og.summit19labs.com', 'jsd-120.og.summit19labs.com', 'jsd-121.og.summit19labs.com', 'jsd-122.og.summit19labs.com', 'jsd-123.og.summit19labs.com', 'jsd-124.og.summit19labs.com', 'jsd-125.og.summit19labs.com', 'jsd-126.og.summit19labs.com', 'jsd-127.og.summit19labs.com', 'jsd-128.og.summit19labs.com', 'jsd-129.og.summit19labs.com', 'jsd-130.og.summit19labs.com', 'jsd-131.og.summit19labs.com', 'jsd-132.og.summit19labs.com', 'jsd-133.og.summit19labs.com', 'jsd-134.og.summit19labs.com', 'jsd-135.og.summit19labs.com', 'jsd-136.og.summit19labs.com', 'jsd-137.og.summit19labs.com', 'jsd-138.og.summit19labs.com', 'jsd-139.og.summit19labs.com', 'jsd-140.og.summit19labs.com', 'jsd-141.og.summit19labs.com', 'jsd-142.og.summit19labs.com', 'jsd-143.og.summit19labs.com', 'jsd-144.og.summit19labs.com', 'jsd-145.og.summit19labs.com', 'jsd-146.og.summit19labs.com', 'jsd-147.og.summit19labs.com', 'jsd-148.og.summit19labs.com', 'jsd-149.og.summit19labs.com', 'jsd-150.og.summit19labs.com', 'jsd-151.og.summit19labs.com', 'jsd-152.og.summit19labs.com', 'jsd-153.og.summit19labs.com', 'jsd-154.og.summit19labs.com', 'jsd-155.og.summit19labs.com', 'jsd-156.og.summit19labs.com', 'jsd-157.og.summit19labs.com', 'jsd-158.og.summit19labs.com', 'jsd-159.og.summit19labs.com', 'jsd-160.og.summit19labs.com', 'jsd-161.og.summit19labs.com', 'jsd-162.og.summit19labs.com', 'jsd-163.og.summit19labs.com', 'jsd-164.og.summit19labs.com', 'jsd-165.og.summit19labs.com', 'jsd-166.og.summit19labs.com', 'jsd-167.og.summit19labs.com', 'jsd-168.og.summit19labs.com', 'jsd-169.og.summit19labs.com', 'jsd-170.og.summit19labs.com', 'jsd-171.og.summit19labs.com', 'jsd-172.og.summit19labs.com', 'jsd-173.og.summit19labs.com', 'jsd-174.og.summit19labs.com', 'jsd-175.og.summit19labs.com', 'jsd-176.og.summit19labs.com', 'jsd-177.og.summit19labs.com', 'jsd-178.og.summit19labs.com', 'jsd-179.og.summit19labs.com', 'jsd-180.og.summit19labs.com', 'jsd-181.og.summit19labs.com', 'jsd-182.og.summit19labs.com', 'jsd-183.og.summit19labs.com', 'jsd-184.og.summit19labs.com', 'jsd-185.og.summit19labs.com', 'jsd-186.og.summit19labs.com', 'jsd-187.og.summit19labs.com', 'jsd-188.og.summit19labs.com', 'jsd-189.og.summit19labs.com', 'jsd-190.og.summit19labs.com', 'jsd-191.og.summit19labs.com', 'jsd-192.og.summit19labs.com', 'jsd-193.og.summit19labs.com', 'jsd-194.og.summit19labs.com', 'jsd-195.og.summit19labs.com', 'jsd-196.og.summit19labs.com', 'jsd-197.og.summit19labs.com', 'jsd-198.og.summit19labs.com', 'jsd-199.og.summit19labs.com', 'jsd-200.og.summit19labs.com']
#instance_list = ['jsd-003.og.summit19labs.com','jsd-004.og.summit19labs.com']
instance_id_list = []
instance_d = {}
region_nm = 'us-west-2'

client = boto3.client('ec2',region_name=region_nm)
#get all instance id's from the instance name list and append to instance_id list to create list of instances to be deleted
for instance in instance_list:
	response = client.describe_instances(
		Filters=[ 
			{
				'Name':'tag:Name',
				'Values':[instance],
			},
			]
		)
	#print (response)
	#print (response['Reservations'][0]['Instances'][0]['InstanceId'])
	instance_id_list.append(response['Reservations'][0]['Instances'][0]['InstanceId'])
	instance_d[instance] = response['Reservations'][0]['Instances'][0]['InstanceId']

print (instance_id_list)
#print (instance_d) #create a dict of instance names and instance id's for troubleshooting purposes.

try:
	delete_response = client.terminate_instances(
		InstanceIds=instance_id_list,
		DryRun = False
			)
	print (delete_response)
except ClientError as e:
	print ('Received Error: %s', e)
	exit(0)




