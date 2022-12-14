from kafka import KafkaConsumer, KafkaProducer
#from confluent_kafka.admin import AdminClient, NewTopic
from kafka.admin import KafkaAdminClient, NewTopic


BROKER_URL = ["b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092",
                                                   "b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092"]

TOPIC = "null"


def consumer(topic):
    kafka_admin = KafkaAdminClient({"bootstrap.servers": BROKER_URL})
    # print(kafka_admin.list_topics().topics)
    # print(topic)
    """
    Consume messages from the topic
    Args:
        topic: The topic to consume from
    """

    c = KafkaConsumer(
        {
            "bootstrap.servers": BROKER_URL,
            "group.id": "121",
            "auto.offset.reset": "latest",
        }
    )

    c.subscribe([topic])
    running = True
    # logger.info("Consumer started")
    poll_timeout = 0
    while running:
        msg = c.poll(1.0)

        if poll_timeout == 20:
            running = False
            break

        if msg is None:
            poll_timeout = poll_timeout + 1
            print("No message received", poll_timeout)
            # logger.debug("No message received")
        elif msg.error() is not None:
            # logger.error(msg.error())
            running = False

        else:
            poll_timeout = 0
            # Get the message from Kafka
            msg_value = msg.value()
            # decode the message
            msg_value = msg_value.decode("utf-8")

            print(f"Received message: {msg_value}")


if __name__ == "__main__":
    consumer(TOPIC)