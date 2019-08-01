# coding=utf-8
# 抽取独立的参数拼装模块
import time

from gatlin.preps import device


# 通用参数map拼装
def genericPackParam():
    param = {}
    param["bizContent"] = "{}"  # 业务数据
    param["countryCode"] = "+63"  # 区号
    param["pageName"] = "index.html"
    param["token"] = ""
    param["hostApp"] = "PHLLOAN"  # 宿主APP
    param["version"] = "1.0.0"
    param["timestamp"] = str(int(time.time() * 1000))
    param["charset"] = "UTF-8"
    param["sign"] = ""
    param["custNo"] = ""
    param["productCode"] = "PHLLOAN"  # 产品编码
    param["signType"] = "RSA"
    param["appVersion"] = "1.0.0"
    param["channelSource"] = "PHL_000"  # 渠道来源
    param["sourceType"] = "APK"  # 来源类型
    param["networkType"] = "wifi"
    # dv = device.packAndroidDevice()
    dv = device.packIosDevice()  # 设备，可选iOS或Android
    param["deviceInfo"] = str(dv)
    param["wifiMac"] = "B0:E5:ED:F6:39:58"
    param["subChannel"] = ""
    param["h5Version"] = "1010199999"
    return param


if __name__ == '__main__':
    print(genericPackParam())
