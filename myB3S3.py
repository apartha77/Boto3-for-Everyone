# Test Boto3 code here
import json
import boto3

print("hellow world")
# #use S3
s3 = boto3.resource('s3')
#for bucket in s3.buckets.all():
#    print(bucket.name)
    
# Upload a new file
data = open("../environment/Boto/Test.txt", "rb")
s3.Bucket('1-bucket-a1').put_object(Key='Test.txt', Body=data)

for bucket in s3.buckets.all():
    if bucket.name == "1-bucket-a1":
        print(bucket.name)
        for files in bucket.objects.all():
            print(files)
    else:
        continue


# largest = None
# print('Before:', largest)
# for itervar in [5, 41, 12, 3, 9, 74, 15]:
#     if largest is None or itervar > largest:
#         largest = itervar
#     print('Loop:', itervar, largest)
# print('Largest:', largest)
