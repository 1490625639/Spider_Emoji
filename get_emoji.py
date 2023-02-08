# -*- coding:utf-8 -*-
"""
作者：张以白(Company)
日期：2023年02月08日
"""
# 导包
import requests
import os
from lxml import etree
num=0


url = "https://p3-pc-sign.douyinpic.com/obj/tos-cn-i-tsj2vxp0zn/f67a5b5d17a6495292dfcc62821666d7?x-expires=1991203200&x-signature=iLXzb41lpf0rYcNeYC31BNKYorA%3D&from=876277922"
# UA伪装
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
# 发送请求，并以content形式响应
page_content = requests.get(url=url, headers=headers).content
with open("./Emoji/a.jpg","wb") as fp:
    fp.write(page_content)
print(page_content)
# # 实例化创建一个etree对象
tree = etree.HTML(page_content)
# # 属性定位，采用xpath定位，这里定位本页所有简历的详情地址，返回值是列表形式
#div_list = tree.xpath("//*[@id='merge-all-comment-container']/div/div[5]/div[2]/div/div[3]/div/div/")
#div_list = tree.xpath("//*[@id='root']/div[1]/div[1]/div[1]/div/@class/text()")

#print(div_list)
# # 二层循环，主要用于下载以及添加文件名字
# for i in div_list:
#     # print(div_list)
#     newurl = i
#     # 获取每个简历的详情界面并发送请求，UA伪装，以及获取响应信息
#     request = requests.get(url='https:' + i, headers=headers)
#     response_text = request.content
#     # 对简历的详情界面进行解析，主要用于解析到下载地址
#     newtree = etree.HTML(response_text)
#     downloadtree = newtree.xpath("//*[@id='down']/div[2]/ul/li[1]/a/@href")[0]
#     # name=newtree.xpath("/html/body/div[6]/div[2]/div[2]/div[1]/div[1]/h1")[0]
#     print(downloadtree)
#     # 对解析出的下载地址发送请求，请求成功后进行下载
#     downzip = requests.get(url=downloadtree, headers=headers).content
#     # 创建一个文件夹
#     try:
#         if not os.path.exists('./简历下载文件'):
#             os.mkdir("./简历下载文件")
#     except:
#         print("wushi")
#     # 对简历的文字信息进行解析，主要用于解析出简历名字，并且作为文件名使用。
#     name = newtree.xpath("//*[@class='ppt_tit clearfix']/h1/text()")[0] + ".rar"
#     # 以解析出的文件名储存到文件夹中
#     filename = "简历下载文件/" + name
#
#     # 文件的下载
#     with open(filename, 'wb')as fp:
#         fp.write(downzip)
#         print("下载成功，文件名为" + name)
#
#         num+=1
# print("下载完成,本次一共下载%d个文件"%num)
#
# """"有个从etree中获取的列表，想依次吧这个的值输出，但是整型跟这个不能用
# 是否可以写一个for i in liebiao  print(" "+i)进行实现呢"""
