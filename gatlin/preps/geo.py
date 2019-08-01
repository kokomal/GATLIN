# coding=utf-8

# 地理定位mock
'''
{
    "province":"",
    "zipcode":"",
    "city":"",
    "country":"",
    "altitude":"7.129120826721191",
    "latitude":"31.21495114566012",
    "addrInfo":"",
    "area":"",
    "longitude":"121.62549304026481"
}'''


def packGeo():
    geog = {}
    geog["province"] = "Guangdong"
    geog["zipcode"] = "523000"
    geog["city"] = "DongGuan"
    geog["country"] = "China"
    geog["altitude"] = "20.123123"
    geog["latitude"] = 22.21495114566012
    geog["addrInfo"] = "Zu Chong Zhi Lu, Pudong Xinqu, Shanghai Shi, China, 201203"
    geog["area"] = "ChengquPianqu"
    geog["longitude"] = 112.62549304026481
    return geog

if __name__ == '__main__':
    print(packGeo())