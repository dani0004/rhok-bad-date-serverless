import boto3
import botocore

import uuid
import re
from hashlib import md5


regex = os.environ['FILE_REGEX']
client=boto3.client('dynamodb')

#the entry point for hte lambda function
def lambda_handler(event, context):
    s3_key = None
    try:
        s3 = boto3.resource('s3')
        s3_key = event['Records'][0]['s3']['object']['key']
        bucket_name =  event['Records'][0]['s3']['bucket']['name'].translate({ord(c):'+' for c in '-:'})
        if not re.match(regex, bucket_name):
            return {'message' : 'Object did not pass filter, not hasing'}
        bucket = s3.Bucket(bucket_name)
        path = pull_file(s3_key, bucket)
        file_hash = hash_file(path)
        if not file_hash:
            raise
        if not insert_hash(file_hash, s3_key, bucket_name):
            raise
    except Exception as e:
        print('Error while hashing file, and inserting to DynamoDB')
        print(e)
        return {'message' : 'Uanble to has and insert {}/{} to database'.format(bucket_name, s3_key)}

    return {'message' : '{} hashed and inserted to database'.format(s3_key)}
	
def create_incident(hashmap incidentInfo,uuid uuid)	
{
	try:		
	tablename='incident_report'
	
	stringInfo={'incident_id'=incidentinfo[0], 
				'submitter_id'=incidentinfo[1]
				'updated'=incidentinfo
				'incident_date'=incidentinfo[4]
				'incident-type'=incidentinfo[6]
				'incident_descriptor'=incidentinfo[7]
				}
	response=client.put_item(tablename,stringInfo)
	
	except Exception as e:
        print('Error while  inserting to DynamoDB')
        print(e)
       // return {'message' : 'Uanble to  insert {}/{} to database'.format(tablename, s3_key)
}

