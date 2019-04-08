from bottle import get, route, run, template, static_file

#  ------ routes ---------
@get('/')
def index():
    return template('news.html')

run(host='localhost', port=8080, debug=True)