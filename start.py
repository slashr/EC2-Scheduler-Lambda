import boto3
import logging

#Simple logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Create EC2 connection object
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):

	#Filter instance having specified tag and status running
	filter = [{'Name': 'tag:AutoStop', 'Values': ['Yes', 'yes', 'YES']}, {'Name': 'instance-state-name','Values': ['stopped']}]
	instances = ec2.instances.filter(Filters=filter)

	#Get IDs of all running and tagged instances
	instance_ids = [instance.id for instance in instances]

	#Print list of instances that will be stopped to logs
	print instance_ids

	if len(instance_ids) > 0:
		#Stop instances
		starting_instances = ec2.instances.filter(InstanceIds=instance_ids).start()
		print starting_instances
	else:
		print "No instances to be started found"
