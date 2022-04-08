# Test Boto3 code with SQS - create, update queue - 5 seconds to wait before an queue item may be processed.
import json
import boto3

#print("Creating a SQS")
# use sqs object - Get the service resource
sqs = boto3.resource('sqs')
# Create the queue. This returns an SQS.Queue instance - 5 seconds wait
#queue = sqs.create_queue(QueueName='TestQ', Attributes={'DelaySeconds': '5'})

# Access queue identifiers and attributes
# print(queue.url)
# print(queue.attributes.get('DelaySeconds'))

# Working with existing SQS
print("Access existing SQS")

# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='TestQ')
# print attributes of queue
# print("URL", queue.url)
# print(queue.attributes.get('QueueArn'))
# print(queue.attributes.get('DelaySeconds'))

# Create a new message
# response = queue.send_message(MessageBody='hello world')
# # The response is NOT a resource, but gives you a message ID and MD5
# print(response.get('MessageId'))
# print(response.get('MD5OfMessageBody'))

# response = queue.send_message(MessageBody='boto3', MessageAttributes={
#     'Author': {
#         'StringValue': 'PSD',
#         'DataType': 'String'
#     }
# })
# print(response.get('MD5OfMessageBody'))
# # Print out any failures
# print(response.get('Failed'))

#Read the messages and delete from the SQS
# Process messages by printing out body and optional author name
for message in queue.receive_messages(MessageAttributeNames=['Author']):
    # Get the custom author message attribute if it was set
    author_text = ''
    if message.message_attributes is not None:
        author_name = message.message_attributes.get('Author').get('StringValue')
        if author_name:
            author_text = ' ({0})'.format(author_name)
    
    # Print out the body and author (if set)
    print('Hello, {0}!{1}'.format(message.body, author_text))
        
    # Let the queue know that the message is processed
    message.delete()
