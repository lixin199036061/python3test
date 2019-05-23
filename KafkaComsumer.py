# -*- coding: utf-8 -*-
from pykafka import KafkaClient
from pykafka.common import OffsetType
import datetime

# -*- coding: utf-8 -*-

def KafkaDownloader(host_, topic_, group_id_):
    client = KafkaClient(hosts=host_)
    _topic = client.topics[bytes(topic_.encode())]
    consumer = _topic.get_simple_consumer(
        consumer_group=bytes(group_id_.encode()),
        auto_commit_enable=False,
        auto_offset_reset=OffsetType.LATEST,
        reset_offset_on_start=True
    )
    if consumer is not None:
        for message in consumer:
            if message is not None:
                print(message.value)
                yield message.value


def get_kafka_data():
    write_file = open("itv_pm_data_1.txt", "w", encoding="utf8")
    TOPIC = "testtopic"
    HOSTS = "192.168.1.21:9092"
    GROUP = ""
    dict_msg = {}

    for message in KafkaDownloader(HOSTS, TOPIC, GROUP):
        # coding: utf-8
        valuestr = message.decode('ascii')

        write_file.write(valuestr + "\n")
        write_file.flush()
        #curr_time = str(datetime.datetime.now())[0:len("2019-04-09 18:26")]
        #msg = message.decode("GB18030")
        #msg_str = str(msg).strip().split("\t")
        #id = msg_str[5]
        #dict_msg.setdefault(id, str(msg).strip())
        #if curr_time == end_time:
        #for key, value in dict_msg.items():
        #    write_file.write(value + "\n")
        #    break
    dict_msg = {}
    write_file.close()


if __name__ == '__main__':
    get_kafka_data()


