from app import microblog

@application.route('/')
@application.route('/index')
def index():
    print("Hello, world!")
