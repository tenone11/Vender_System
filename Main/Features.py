from pyecharts import charts
import re, os, Main


def create_bar(x_list, y_list):
    bar = charts.Bar()
    bar.add_xaxis(x_list)
    for i in y_list:
        bar.add_yaxis(i[0], i[1])
    bar.render("Main/Source/bar.html")


def legal_url(html_name):
    root_path = os.path.abspath(os.path.dirname(__file__))
    url_string = "file:///%s/Source/%s.html" % (root_path, html_name)
    url_string = re.sub(r'\\', '/', url_string)
    return url_string

# def set_function_content('a*b=c;x+y=z'):
#     Main.function_content = []



class Features:
    def __init__(self, pd_dict):
        self.pd_dict = pd_dict

    def get_base_sum(self, vendor_list, which_col):
        result = []
        for i in vendor_list:
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
        # [公司名], [项目名s], [qians]


