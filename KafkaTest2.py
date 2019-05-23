

from pykafka import KafkaClient


client = KafkaClient(hosts="192.168.1.90:9092")
print(client.topics)
topic = client.topics[b'testtopic']    #topic名称
consumer = topic.get_simple_consumer()
for record in consumer:
    if record is not None:
        valuestr = record.value.decode()   #从bytes转为string类型
        valuedict = eval(valuestr)
        message = valuedict["message"]
        fields = message.split("\u0001")
        for field in fields:
            kv = field.split("\u0002")
            if len(kv) == 2:
                print(kv[0],'----',kv[1])
        print('-'*100)

