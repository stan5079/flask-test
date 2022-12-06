from flask import Flask, render_template, request


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get('/')
    def get() -> str:
        return render_template('test.html')

    @app.post('/post')
    def post() -> str:
        print(request.data)
        print(request.form)
        print(request.files)
        return ''

    return app
