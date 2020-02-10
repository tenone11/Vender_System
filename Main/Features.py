from pyecharts import charts
import re, os, json


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

    def run_function(self, val):  # 函数输入值
        _list = []
        result = []
        if re.search(';', val):
            _list = [i for i in val.split(';') if i != '']  # 'a*b=c;x+y=z' > ['平均人天=总人天/个数', 'x+y=z']
        else:
            _list.append(val)
        _dict = {}
        _dict.setdefault('Function_Content', _list)
        new = json.dumps(_dict, sort_keys=True, indent=4, separators=(',', ': '))
        print(new)
        try:
            with open('./Main/Source/data.json', 'w', encoding='utf-8') as f:
                f.write(new)
        except Exception as e:
            print(e)
        # print(val)
        # head_list = [column for column in pd_dict]   # ['公司名称', ...,'单笔支付']
        for func in _list:   # ['凭证字号*类型=执行部门', 'x+y=z']
            # print(func)    # '平均人天=总人天/个数;付款金额=不含税金额*税率'
            self.pd_dict.eval(func, inplace=True)
            result_name = func.split('=')[0]    # '平均人天'
            result.append(result_name)
        print(result)
        return result
