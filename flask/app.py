from flask import Flask,render_template,request
flask=Flask(__name__)
@flask.route('/')
def display():
    if request.method == 'POST':
        if request.form['username']=='admin' and request.form['password']=='1234':
            return render_template('dash.html')
        else:
            return render_template('home.html',error='Invalid credentials')
    return render_template('home.html')
@flask.route('/dashboard')
def dashboard():
    return render_template('dash.html')
@flask.route('/welcome')
def function_greet():
    return f"""
    <h2>
        <div class="p-3 text-primary-emphasis bg-primary-subtle border border-primary-subtle rounded-3 text-center">
            Verify,Will Your Knowledge Make You Placed
        </div>
    </h2>
    """
if __name__=="__main__":
    flask.run(debug=True)