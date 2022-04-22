#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'smilebin'

import requests
import json
import re
import time

from user_agent import generate_user_agent

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class ExpressOfBaidu:
    """
    模拟从百度上查询快递信息.
    """

    def __init__(self):
        self.cookies = ""
        self.tokenV2Url = ""
        self.userAgent = generate_user_agent()

    def getTokenV2(self, nu):
        """
        模拟输入框输入快递单号, 从结果中拿到TokenV2值
        """
        url = f"https://www.baidu.com/s?wd={nu}"

        payload = {}
        headers = {
            'User-Agent': self.userAgent
        }

        start_time = time.time()

        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        end_time = time.time()
        print("耗时1: {:.2f}秒".format(end_time - start_time))

        rep_text = response.text

        start_time = time.time()
        rep_text = rep_text.replace("\r", "").replace("\n", "")
        end_time = time.time()
        print("耗时2: {:.2f}秒".format(end_time - start_time))

        reg = re.compile('.*apiUrl: \'(.*)\', +?apiUrlT.*')
        mtch = reg.match(rep_text)
        print(self.userAgent)
        if mtch is not None:
            self.cookies = response.cookies.get_dict()
            return mtch.group(1)
        else:
            print(rep_text)
            return ""

    def getExpressInfo(self, nu):
        """
        查询快递单号(自动匹配快递公司)
        """
        # 先获取一下TokenV2的值
        if self.tokenV2Url == "":
            self.tokenV2Url = self.getTokenV2(nu)

        if self.tokenV2Url == "":
            return {}

        payload = {}
        cookieStr = ""
        for k, v in self.cookies.items():
            cookieStr = cookieStr + k + "=" + v + ";"

        headers = {
            'Cookie': cookieStr,
            'User-Agent': self.userAgent
        }

        start_time = time.time()
        self.tokenV2Url = self.tokenV2Url + f"&appid=4001&nu={nu}&_={str(int(time.time() * 1000))}"

        response = requests.request("GET", self.tokenV2Url, headers=headers, data=payload, verify=False)
        end_time = time.time()
        print("耗时3: {:.2f}秒".format(end_time - start_time))
        # response.encoding="utf-8"
        resp_text = response.text.replace("\\/", "/")
        resp_text = resp_text.encode('latin-1').decode('unicode_escape')
        resp_json = json.loads(resp_text)

        if "data" in resp_json and "info" in resp_json["data"]:
            return resp_json["data"]["info"]
        else:
            return {}


expressapi = ExpressOfBaidu()
print(expressapi.getExpressInfo("312130253984875"))
