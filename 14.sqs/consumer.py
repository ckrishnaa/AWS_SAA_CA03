import json

import boto3

sqs = boto3.client("sqs", region_name="ap-southeast-2")

url = "https://sqs.ap-southeast-2.amazonaws.com/577702170675/simple-queue"

sent = sqs.send_message(
    QueueUrl=url,
    MessageBody=json.dumps({"orderId": 101, "item": "biryani"}),
    MessageAttributes={"source": {"DataType": "String", "StringValue": "web"}},
)
print("sent    ", sent["MessageId"])

input("Wait 1")

got = sqs.receive_message(
    QueueUrl=url, MessageAttributeNames=["All"], WaitTimeSeconds=5
)["Messages"][0]


print(
    "received",
    json.loads(got["Body"]),
    "source =",
    got["MessageAttributes"]["source"]["StringValue"],
)
input("Wait 2")
sqs.delete_message(QueueUrl=url, ReceiptHandle=got["ReceiptHandle"])
a = sqs.get_queue_attributes(QueueUrl=url, AttributeNames=["All"])["Attributes"]
print(
    "after delete:",
    a["ApproximateNumberOfMessages"],
    "waiting,",
    a["ApproximateNumberOfMessagesNotVisible"],
    "hidden",
)

# sqs.delete_queue(QueueUrl=url)
