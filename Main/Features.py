from pyecharts import charts
import re, os, json, shutil


def create_bar(x_list, col_name, y_list):
    bar = charts.Bar()
    bar.add_xaxis(x_list)
    bar.add_yaxis(col_name, y_list)
    bar.render("Main/Sources/bar.html")

def create_pie( col_name, y_list):
    pie = charts.Pie()

    pie.add(col_name, y_list)
    pie.render("Main/Sources/pie.html")

def legal_url(html_name):
    root_path = os.path.abspath(os.path.dirname(__file__))
    url_string = "file:///%s/Sources/%s.html" % (root_path, html_name)
    url_string = re.sub(r'\\', '/', url_string)
    return url_string

def save_file(source, target):
    shutil.copyfile(source, target)

class Features:
    def __init__(self, pd_dict):
        self.pd_dict = pd_dict

    def get_col_list(self, col_name):
        result = self.pd_dict.drop_duplicates(subset=[col_name], keep='first')
        result = result[col_name].dropna().tolist()
        if '' in result:
            result.remove('')
        return result

    def get_one_col_sum(self, col_name):
        return self.pd_dict[col_name].sum()

    def filter_one_col_sum(self, col_name, which_col):
        result = []
        for i in self.get_col_list(col_name):
            temp = self.pd_dict[self.pd_dict[col_name] == i]
            result.append([i, temp[which_col].sum()])
        # print(result)
        return result

    def get_project_sum(self, filter01, filter02, val):
        result = []
        temp = self.pd_dict[self.pd_dict[filter01] == vendor_name]
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
        with open('./Main/Sources/data.json', 'w', encoding='utf-8') as f:
            f.write(new)
        # head_list = [column for column in pd_dict]   # ['公司名称', ...,'单笔支付']
        for func in _list:  # ['凭证字号*类型=执行部门', 'x+y=z']
            # print(func)    # '平均人天=总人天/个数;付款金额=不含税金额*税率'
            self.pd_dict.eval(func, inplace=True)
            result_name = func.split('=')[0]  # '平均人天'
            result.append(result_name)
        return result
