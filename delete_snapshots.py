#python code to delete RDS snapshots

import boto3
import json
import botocore

db_file = '/Users/arajagopalan/rds_snapshot_out.json' #json output of the aws cli command - aws rds describe-db-snapshots --output=json --max-items=10 --region=us-west-2 > {filename}
db_snap_list = []
db_snap_list_us_west_2a = []
db_snap_list_us_west_2b = []
db_snap_list_us_west_2c = []
db_snap_list_us_west_2d = []

region_nm = 'us-west-2'

with open (db_file,'r') as f:
	doc = json.load(f)
#print (doc)
#print (doc['DBSnapshots'])

for d in range(0,len(doc['DBSnapshots'])):
	#print (d)
	#print (doc['DBSnapshots'][d])
	db_snap_list.append(doc['DBSnapshots'][d]['DBSnapshotIdentifier'])
	'''
	if doc['DBSnapshots'][d]['AvailabilityZone'] == 'us-west-2a':
		db_snap_list_us_west_2a.append(doc['DBSnapshots'][d]['DBSnapshotIdentifier'])
	elif doc['DBSnapshots'][d]['AvailabilityZone'] == 'us-west-2b':
		db_snap_list_us_west_2b.append(doc['DBSnapshots'][d]['DBSnapshotIdentifier'])
	elif doc['DBSnapshots'][d]['AvailabilityZone'] == 'us-west-2c':
		db_snap_list_us_west_2c.append(doc['DBSnapshots'][d]['DBSnapshotIdentifier'])
	elif doc['DBSnapshots'][d]['AvailabilityZone'] == 'us-west-2d':
		db_snap_list_us_west_2d.append(doc['DBSnapshots'][d]['DBSnapshotIdentifier'])


print ('List of database snapshots in US-WEST-2A %s' % db_snap_list_us_west_2a)
print ('Number of snapshots in US-WEST-2A is', len(db_snap_list_us_west_2a))
print ('List of database snapshots in us-west-2B %s' % db_snap_list_us_west_2b)
print ('Number of snapshots in US-WEST-2B is', len(db_snap_list_us_west_2b))
print ('List of database snapshots in US-WEST-2C %s' % db_snap_list_us_west_2c)
print ('Number of snapshots in US-WEST-2C is', len(db_snap_list_us_west_2c))
print ('List of database snapshots in US-WEST-2D %s' % db_snap_list_us_west_2d)
print ('Number of snapshots in US-WEST-2D is', len(db_snap_list_us_west_2d))
'''
print ('List of database snapshots is %s' % db_snap_list)
print ('Number of snapshots is', len(db_snap_list))


client = boto3.client('rds',region_name=region_nm)


for snapshot in db_snap_list:
	try:
		print ('Deleting snapshot %s' % snapshot)
		response = client.delete_db_snapshot(
			DBSnapshotIdentifier=snapshot
			)
		print (response)
		print ('DBSnapshot %s has been deleted' % response['DBSnapshot']['DBSnapshotIdentifier'])
	except botocore.exceptions.ClientError as e:
		#print (e.response['Error']['Code'])
		#print (e)
		if e.response['Error']['Code'] == 'DBSnapshotNotFound':
			print ('DBSnapshot %s is not found or already deleted' % snapshot)
exit(0)

