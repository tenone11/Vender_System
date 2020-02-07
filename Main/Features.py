from pyecharts import charts
from datetime import datetime


class Features:
    def __init__(self, pd_dict):
        self.pd_dict = pd_dict

    def get_y_m(self, selected_item):
        format_date = datetime.strptime(selected_item, '%Y-%m-%d').strftime("%Y-%m")
        return format_date

    def get_y(self, selected_item):
        format_date = datetime.strptime(selected_item, '%Y-%m-%d').strftime("%Y")
        return format_date


    def create_bar(self, x_list, y_list):
        bar = charts.Bar()
        bar.add_xaxis(x_list)
        for i in y_list:
            bar.add_yaxis(i[0], i[1])
        bar.render("Main/Source/bar.html")

    def get_base_sum(self, which_col):
        vender_list = list(set(self.pd_dict['公司名称']))
        result = []
        for i in vender_list:
            temp = self.pd_dict[self.pd_dict['公司名称'] == i]
            result.append(temp[which_col].sum())
        return result

    def get_project_sum(self, vendor_name, request, val):
        result = []
        temp = self.pd_dict[self.pd_dict['公司名称'] == vendor_name]
        request_list = list(set(temp[request]))
        for i in request_list:
            result.append(temp[(temp[request] == i)][val].sum())
        return vendor_name, request_list, result
        #[公司名], [项目名s], [qians]