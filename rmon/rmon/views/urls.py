#定义 路由

from flask import Blueprint

from rmon.views.index import IndexView
#名为api 的蓝图
api = Blueprint('api',__name__)
# api 的路由 为 ‘／’，访问／时调用 IndexView 处理 GET， POST
# 通过url_for(‘api.indx'),获得对应的URL
api.add_url_rule('/',view_func=IndexView.as_view('index'))
