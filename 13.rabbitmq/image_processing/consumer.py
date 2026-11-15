import time

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


def process_image(ch, method, properties, body):
    print(f" [x] Processing {body.decode()}")
    time.sleep(2)  # Simulate processing time
    print(f" [x] Finished {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


# Start consuming
channel.basic_consume(queue="image_queue", on_message_callback=process_image)
print(" [*] Waiting for image tasks. To exit press CTRL+C")
channel.start_consuming()
