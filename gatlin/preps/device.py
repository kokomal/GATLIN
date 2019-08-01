# coding=utf-8
'''
设备生成器，基本上不需要改造，除非特殊的手机设备埋点请求要注意
Using PYTHON 3.7.3
Do not use for commercial purposes.
Copyright by Chenyuanjun
All rights reserved
'''
import json

# Android设备
def packAndroidDevice():
    device = {}
    device["terminalType"] = "app"
    device["deviceSn"] = "app"
    device["deviceOs"] = "ANDROID"
    device["deviceOsVersion"] = "7.0"
    device["deviceIp"] = "10.93.146.175"
    device["imsi"] = "460014055609890"
    device["isRoot"] = "N"
    device["isEmulator"] = "N"
    device["networkType"] = "WIFI"
    device["wifiMac"] = "B0:E5:ED:F6:39:58"
    device["wifiName"] = "360Jie"
    device["brand"] = "HONOR"
    device["model"] = "DUK-AL20"
    device["usedStorage"] = "27459276800"
    device["totalStorage"] = "56302223360"
    device["factoryTime"] = "1501216717000"
    device["deviceName"] = "DUK-AL20"
    device["deviceFingerPrintM2"] = "d294f2bbe2e9d10a30b8e7f82b709dde"
    device["deviceFingerPrintM2N"] = "fe2a143c58104253eaa3ffd6d7a6c980"
    device["deviceFingerPrintTd"] = "yJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjMiLCJwYWNrYWdlcyI6ImNvbS5qaW5zaGFuZy5wZGwuYW5kcm9pZF8xLjAuMCIsInByb2ZpbGVfdGltZSI6MTM4LCJ0b2tlbl9pZCI6Ikh2aFAzSDlqVDlSRFVSajl6RkVvT3ZTME1LcldhZ0hcL2VsVEh5cFc2NTdjbEFjMDdKWFRLb3JTc3Blemk4NG12d00wQjVKWXdiQW9kZVAxSGFxTmVkQT09In0="
    device["deviceFingerPrintBr"] = ""
    device["uuid"] = "00000000-7e58-1d92-ffff-ffffe1669361"
    device["bssid"] = "94:28:2e:8f:b9:a0"
    device["isYUNOS"] = "N"
    device["regId"] = ""
    device["androidId"] = "1562e7419dafb885"
    return device


# iOS手机设备
def packIosDevice():
    device = {}
    device["deviceIp"] = "192.168.1.61"
    device["buildSerial"] = "7AD0E1A5-ED63-4240-8C8B-C49845CAD2E5"
    device["deviceFingerPrintM2N"] = "e59b805bf8a90446643319213deb5a0f"
    device["isEmulator"] = "N"
    device["deviceOs"] = "IOS"
    device["bssid"] = "50:fa:84:86:29:b5"
    device["deviceFingerPrintM2"] = "e59b805bf8a90446643319213deb5a0f"
    device["isJailbreaking"] = "N"
    device["imsi"] = "7AD0E1A5-ED63-4240-8C8B-C49845CAD2E5"
    device["deviceFingerPrintTd"] = "eyJ0b2tlbklkIjoibW83QUtuZmU2dDg0WFI2Q3ROZ3dQV3Rvc1dtZE1NZStcL0RSZEFPMk5Lc0JpT0ZVREdjZFY1cHlGVnluNU15dXdCWk1WTTJvcGlrb1VJclU0K21GOVFBPT0iLCJvcyI6ImlPUyIsInByb2ZpbGVUaW1lIjoxOTQsInZlcnNpb24iOiIzLjAuNCJ9"
    device["deviceOsVersion"] = "iOS 11.4"
    device["uuid"] = "3E257053-F594-4B9C-B78B-7447256CED08"
    device["deviceSn"] = "E22C549B-5958-45A4-BE3E-B1F5C30004CC"
    device["deviceName"] = "sciPhone"
    device["totalStorage"] = "29GB"
    device["wifiName"] = "JCFC_5G"
    device["model"] = "iPhone 6s"
    device["networkType"] = "WiFi"
    device["brand"] = "Apple"
    device["usedStorage"] = "0GB"
    device["idfa"] = "7AD0E1A5-ED63-4240-8C8B-C49845CAD2E5"
    device["deviceFingerPrintBr"] = "-"
    device["terminalType"] = "app"
    device["wifiMac"] = "E22C549B-5958-45A4-BE3E-B1F5C30004CC"
    device["regId"] = ""
    return device

if __name__ == '__main__':
    print(json.dumps(packIosDevice()))
    print(json.dumps(packAndroidDevice()))