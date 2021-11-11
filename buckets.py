import boto3


def number_buckets(num):
    client = boto3.client('s3')
    buckets = client.list_buckets()
    count = 0
    for bucket in buckets['Buckets']:
        print(f"Processing bucket number-[{count}]")
        if count < num:
            #print(bucket)
            current_bucket = bucket['Name']
            print(f"Found Bucket: {current_bucket}")
            count +=1
        else:
            return

number_buckets(2)
    
    
    
    