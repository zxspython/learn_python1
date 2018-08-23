# -*- coding: UTF-8 -*-

from flask import request
from flask import Flask
from flask import render_template
from ele import ele_red_packet


app = Flask(__name__)

#了解GET，POST方法。
#GET 方法，获得页面
#POST 方法，request 提交数据。
#request.method 获得提交的方法;request.form［ ］可以获得提交表格的具体参数.
@app.route('/',methods=['GET','POST'])
def phone_number_form():
    if request.method == 'POST':
        phone_number = request.form['phone']
        message = ele_red_packet(phone_number)
    else :
        message = ''
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
