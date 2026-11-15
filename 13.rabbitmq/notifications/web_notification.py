import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="news_alerts_exchange", exchange_type="fanout")

queue_name = "web_notification_queue"
channel.queue_declare(queue=queue_name)
channel.queue_bind(exchange="news_alerts_exchange", queue=queue_name)


def callback(ch, method, properties, body):
    print(f" [Web Notification] Received: {body.decode()}")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
print(" [*] Waiting for news alerts...")
channel.start_consuming()
