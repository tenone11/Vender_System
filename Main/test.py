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

# import re
#
# b={'上海大宁文化传播有限公司': 88, '漕河三维动画有限公司': 46, '成都大老王信息科技有限公司': 29, '成都嘘嘘网络科技有限公司': 14}
# c = ['', '', 'c']
# print([0][0])
#
# youraddress = 'C:\Users\Administrator\PycharmProjects\Vender_System\Main'
# url_string = "file:///%s/Sources/bar.html" % youraddress
# url_string = re.sub(r'\\', '/', url_string)
# print(url_string)
# import pandas as pd
# df = pd.read_excel('e:\\Test\\abc.xlsx')
# print(df)

# val = '我*b=c;x+y=z;'
# if re.search(';', val):
#     list = [i for i in val.split(';') if i != '']
#     print(list)
#     for i in list:
#         re.match('\(+-*/\)', i)
#
# aaa = '平均人天=总人天/个数'
#
# bbb = ['日期', '业务日期', '凭证字号', '游戏项目', '类型', '备注', '申请人', '执行部门']
#
# print(aaa.split('=')[0])
# #['', '', '', '', '-', '()+*=', '/']
# # eval(a)
# import Main
# print(Main.function_content)
from eplot import eplot
import pandas as pd
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Pie


def pie_base() -> Pie:
    c = (
        Pie()
        .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    print ([list(z) for z in zip(Faker.choose(), Faker.values())])
    return c