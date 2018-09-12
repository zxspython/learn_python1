# 整个 应用的首页控制器代码

from flask import render_template
#MethodView 实现了 IndexView ：接受到GET 方法时，会执行get方法，对请求进行处理。
from flask.views import MethodView

class IndexView(MethodView):
    def get(self):
        # render_template 模板渲染
        return render_template('index.html')
