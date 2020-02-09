# from pyecharts.charts import Bar
#
# bar = Bar()
# bar.add_xaxis(["横扫一切", "仙乐传说", "盖世豪杰", "草鸡偶像", "最后幻想", "寻找地狱"])
# bar.add_yaxis("上海大宁文化传播有限公司", [184000.0, 12827105.0, 113300.0, 72500.0, 1074490.0, 154600.0, 112950.0])
#
# # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")
# bar.render()

#
# a = ['上海大宁文化传播有限公司', [113300.0, 72500.0, 154600.0, 12827105.0, 112950.0, 184000.0, 1074490.0]]
# print (a[0])

import re
#
# youraddress = 'C:\Users\Administrator\PycharmProjects\Vender_System\Main'
# url_string = "file:///%s/Source/bar.html" % youraddress
# url_string = re.sub(r'\\', '/', url_string)
# print(url_string)
a= [1,2]
b= [2,3]

val = 'a*b=c;x+y=z;'
if re.search(';', val):
    list = [i for i in val.split(';') if i != '']
    # for i in list:

    print(list)
# eval(a)