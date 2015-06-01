from flask import Flask, url_for
app = Flask(__name__)

@app.route('/profile/<username>')
def show_user_profile(username):
    return 'User: %s ' % username


@app.route('/')
def show_url_for():
    return url_for('show_user_profile', username = 'oscar')

#@app.route('/post/<int:post_id>')
#def show_post(post_id):
    #return 'Post: %d ' %post_id

if __name__ == '__main__':
    app.debug = True
    app.run()
