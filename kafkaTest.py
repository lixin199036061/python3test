
# -*- coding: utf-8 -*-
import json

from kafka import KafkaProducer


def produce():
    producer = KafkaProducer(bootstrap_servers='139.224.239.42:9092,101.132.158.81:9092,47.100.224.81:9092')
    for i in range(8000000):
        msg_dict = {
            "db_config": {
                "database": "test_1",
                "host": "localhost",
                "user": "root",
                "password": "password"
            },
            "table": "msg",
            "msg": "the %s record" % i
        }
        msg = json.dumps(msg_dict)
        print(msg)
        re = producer.send('testtopic', key=b'test', value=msg.encode("utf-8"))
    producer.close()
    print(re)


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

#主函数
def main():
    producer = KafkaProducer(bootstrap_servers='139.224.239.42:9092,101.132.158.81:9092,47.100.224.81:9092')

    msg_dict = {
        "sleep_time": 10,
        "db_config": {
            "database": "test_1",
            "host": "xxxx",
            "user": "root",
            "password": "root"
        },
        "table": "msg",
        "msg": "Hello World"
    }
    msg = json.dumps(msg_dict)
    producer.send('testtopic',key=b'test', value=msg.encode("utf-8"))
    producer.close()


if __name__=="__main__":
    produce()
    print('test')