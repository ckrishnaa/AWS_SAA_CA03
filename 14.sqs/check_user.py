import boto3

REGION = "ap-southeast-2"

who = boto3.client("sts", region_name=REGION).get_caller_identity()
print("account:", who["Account"])
print("you are:", who["Arn"])

sqs = boto3.client("sqs", region_name=REGION)
print("queues :", sqs.list_queues().get("QueueUrls", []))
