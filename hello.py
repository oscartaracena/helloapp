from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "User %s logged in" % request.form['username']
    else:
        return render_template('login.html')


#@app.route('/')
#def show_url_for():
#    return url_for('show_user_profile', username = 'oscar')

#@app.route('/post/<int:post_id>')
#def show_post(post_id):
    #return 'Post: %d ' %post_id

if __name__ == '__main__':
    app.debug = True
    app.run()
