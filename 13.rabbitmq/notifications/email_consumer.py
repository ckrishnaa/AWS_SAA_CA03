import pika

# Establish connection
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Declare exchange
channel.exchange_declare(exchange="news_alerts_exchange", exchange_type="fanout")

# Declare a queue (auto-delete if no consumers)
queue_name = "mobile_app_queue"
channel.queue_declare(queue=queue_name)
channel.queue_bind(exchange="news_alerts_exchange", queue=queue_name)


# Callback function
def callback(ch, method, properties, body):
    print(f" [Mobile App] Received: {body.decode()}")


# Consume messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
print(" [*] Waiting for news alerts...")
channel.start_consuming()
