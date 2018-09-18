from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Andrew'}
    return '''
<html>
    <head>
        <title>Jively Home Page</title>
    </head>
    <body>
        <h1>Welcome to Jively WSNs, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
