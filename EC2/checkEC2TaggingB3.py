import json
import boto3

client = boto3.client('ec2')
snsclient = boto3.client('sns')

def lambda_handler(event, context):
    # Get the instance id from the event - check the event details from event bridge
    #ec2_instance_id = event["EC2InstanceId"]
    ec2_instance_id = event["detail"]["instance-id"]

    print("Printing EC2-ID", ec2_instance_id)
    
    # Code from Boto3 documentation - client is the ec2 here
    response = client.describe_tags(
    Filters=[
        {
            'Name': 'resource-id',
            'Values': [ec2_instance_id]
        },
    ],
    )
    # Print the whole response to verify
    # print("printing response", response)
    # Focus on Tags and find the required Tag - in this example used "Special"
    alltags = response["Tags"]
    # Check with Flag if the required tag is being detected
    flag ="Stop"
    for tag in alltags:
        print(tag["Key"])
        if tag["Key"]=="Special":
            flag="Don't Stop"
            break

    print(flag)
    
    # Decision making - stop the ec2 and send sns
    if flag == "Stop":
        response1 = client.stop_instances(
        InstanceIds=[ ec2_instance_id],
        Force=True
        )
        # Send SNS
        snsarn = "arn:aws:sns:us-east-1:231653829444:EC2-Improper-Tagging"
        mailmessage = "The EC2 " + ec2_instance_id + " is being Stopped due to improper tagging."
        mailsubject = "EC2 Stopped - Team Informed"
        snsresponse = snsclient.publish(
            TopicArn= snsarn,
            Message= mailmessage,
            Subject= mailsubject,
            )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Test EC2 Tags!')
    }
