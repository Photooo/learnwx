# encoding: utf-8
__author__ = 'photooo'

import re
import requests
import time

def get_weixin_uuid():
	url = 'https://login.weixin.qq.com/jslogin'
	pm = {
	'appid' : 'wx782c26e4c19acffb',
	'fun' : 'new',
	'lang' : 'zh_CN',
	'_' : time.time()}
	response = requests.get(url, params = pm)

	wxtext = response.text
	wxpattern = 'window\.QRLogin\.uuid.=."(.+)"'
	wxre = re.compile(wxpattern)
	wxmatch = re.search(wxre, wxtext)
	uuid = wxmatch.group(1)
	return uuid

if __name__ == "__main__":
	uuid = get_weixin_uuid()
	print uuid
