from pyecharts import charts
from datetime import datetime


class Features:
    def get_y_m(self, selected_item):
        format_date = datetime.strptime(selected_item, '%Y-%m-%d').strftime("%Y-%m")
        return format_date

    def get_y(self, selected_item):
        format_date = datetime.strptime(selected_item, '%Y-%m-%d').strftime("%Y")
        return format_date

    def create_bar(self, x_list, vendor_name, val_list):
        bar = charts.Bar()
        bar.add_xaxis(x_list)
        for i in vendor_name:
            bar.add_yaxis(i, vendor_name[val_list])
        # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
        # 也可以传入路径参数，如 bar.render("mycharts.html")
        bar.render("./Source/bar.html")

    def get_sum(self, _list):
        result = 0
        for i in _list:
            try:
                i = float(i)
            except Exception as e:
                continue
            result += i
        return result
a = ['1', '2', 'a ']
b = Features()
c = b.get_sum(a)
print(c)
