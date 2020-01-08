from flask import Flask, request, render_template

# Flask通过render_template()函数来实现模板的渲染。
app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


# 注意这里如果登录失败则会回到登录页面并会有Bad boy消息产生
if __name__ == '__main__':
    app.run()
