import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Declare exchange and queue
channel.exchange_declare(exchange="task_exchange", exchange_type="direct")
channel.queue_declare(queue="image_queue")

# Bind queue to exchange
channel.queue_bind(
    exchange="task_exchange", queue="image_queue", routing_key="image_task"
)

# List of images to process
images = ["image1.jpg", "image2.jpg", "image3.jpg"]

for image in images:
    channel.basic_publish(
        exchange="task_exchange", routing_key="image_task", body=image
    )
    print(f" [x] Sent {image}")

connection.close()
