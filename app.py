from flask import Flask, render_template, request, session
from babel import numbers, dates
from datetime import datetime, date, time
from flask_babelex import Babel, Domain
# from flask_babel import Babel
from flask_admin.babel import gettext
from flask_admin import translations

SUPPORTED_LANGUAGES = ['en', 'zh_CN', 'zh_TW']

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
# babel = Babel(app, default_domain=Domain(translations.__path__[0], domain='admin'))
babel = Babel(app, default_domain=Domain('translations', domain='admin'))

@babel.localeselector
def get_locale():
    accept_language = request.accept_languages.best_match(SUPPORTED_LANGUAGES)
    override = request.args.get('lang')
    if override:
        session['lang'] = override
    # return 'zh_CN'
    print(session['lang'])
    return session.get('lang', accept_language)

@app.route('/')
def hello_world():
    d = date(2020, 1, 2)
    dt = datetime(2020, 1, 2, 18, 19)

    zh_date = dates.format_date(d, locale='zh_CN')
    us_date = dates.format_date(d, locale='en_US')

    # gettext('123')

    return render_template('index.html',
                           zh_date=zh_date,
                           us_date=us_date)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002, debug=True)
