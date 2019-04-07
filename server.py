from bottle import get, route, run, template, static_file

#  ------ routes ---------
@get('/')
def index():
    return template('news.html')

# ------- static files --------
@route('/css/<filename>')
def send_css_file(filename):
    return static_file(filename, root='css')

@route('/images/<filename>')
def send_image(filename):
    return static_file(filename, root='images')

run(host='localhost', port=8080, debug=True)