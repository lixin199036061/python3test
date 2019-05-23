import pymongo
import json
import datetime

# 配置数据库信息
MONGO_URl = 's-uf677a8f6813de54-pub.mongodb.rds.aliyuncs.com:3717'
MONGO_DB = 'ibike_pt' # 数据库名
MONGO_TABLE = 'draw_bike' # 表名

# 连接数据库
client = pymongo.MongoClient(MONGO_URl)
db = client[MONGO_DB]

# 存入数据库
def save_url_to_Mongo(result):

    dict ={}
    #json对象
    json_str = json.dumps(result)
    #print('trst:    '+json_str)

    #词典
    data2 = json.loads(json_str)
    #print(data2)

    db.authenticate('ibike', 'Eversafe123!')
    account = db.get_collection("draw_bike")

    account.update_one({"name": "zhangsan"}, {"$set": {"age": "28"}})

    #写自定义的时间进mongodb
    date2 = datetime.datetime.strptime("2019-04-10 12:00:48", "%Y-%m-%d %H:%M:%S")

    dict['not_in_p']=1
    dict['low_power']=1
    dict['out_maintance_area']=1
    dict['zombie_bike']=1
    dict['zombie_days']=1
    dict['system_fault']=1
    dict['boss_fault']=1
    dict['last_lend_time']=datetime.datetime.utcnow()
    dict['last_return_time']=date2



    #{mydate:ISODate("2019-04-02 07:58:51")}


    #account.insert_one({"testtime":datetime.datetime.utcnow()})

    #if account.insert_one(result):
    #    print('存储到MongoDB成功', result)

    #读出来的就是一个词典
    lsit = account.find({'c_bikeno':'02271123'})
    for i in lsit:

        #i['c_bluename']='02271125'
        print(i)

        account.update_one({'c_bikeno':'02271123'}, {"$set": dict})

        account.update_one({'c_bikeno':'02271123'}, {"$set": {"age":32}})







    #for i in account.find({"name": "xxx"}):
    #if account.insert_one(result):
    #    print('存储到MongoDB成功', result)




if __name__ == '__main__':
    save_url_to_Mongo({
        "_class" : "com.ibike.mongo.domain.BikeLock",
        "c_bikeno" : "02271123",
        "c_bikelong" : 119.968574829618,
        "c_bikelat" : 31.8394336156862,
        "c_serialno" : 1123,
        "c_type" : 14,
        "c_lasttime" : "2018-10-07 09:15:33.722",
        "c_state" : 1,
        "c_addtime" : "2018-09-06 12:55:10.588",
        "loc" : {
            "type" : "Point",
            "coordinates" : [
                119.968574829618,
                31.8394336156862
            ]
        },
        "batchId" : "0227",
        "c_citycode" : "519001",
        "c_blueVersion" : "0A06",
        "shNo" : "566",
        "ccid" : "89860402101770099573",
        "imei" : "868183034232525",
        "c_blueID_android" : "252523343018",
        "version" : "7.0.18",
        "voltage" : 0.239999994635582,
        "gpstime" : "2019-03-25 22:08:51",
        "lockState" : "cc",
        "bleVersion" : "3.0.4",
        "bmsPercent" : 0,
        "updateTime" : "2019-03-25 22:08:53",
        "regionId" : "533",
        "lon" : 119.968574829618,
        "lat" : 31.8394336156862,
        "sn" : "",
        "bmsCapacity" : 0,
        "orderno" : "D0EC1EFE3B16624A0549",
        "locSource" : "3",
        "inRail" : "2",
        "inPark" : "2",
        "c_blueE" : "35.844",
        "c_blueV" : "35.844",
        "railVersion" : 0,
        "c_bluename" : "02271123",
        "online" : "0",

    })
