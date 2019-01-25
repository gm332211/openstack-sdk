#-*- coding: utf-8 -*-
# @Author:xiaoming
msg = "北京"
# print(msg.encode(encoding = "utf-8"))#unicode编码转换为utf-8编码
# print(msg.encode(encoding = "utf-8").decode(encoding = "utf-8"))#unicode编码转换为utf-8编码，再转化为unicode编码
test=msg.decode('utf-8')
print(type(test))