import pika

# Establish connection
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Declare a fanout exchange
channel.exchange_declare(exchange="news_alerts_exchange", exchange_type="fanout")

# Publish a message
message = "Breaking News: Major event happening now!"
channel.basic_publish(exchange="news_alerts_exchange", routing_key="", body=message)

print(f" [x] Sent: {message}")

# Close connection
connection.close()
