@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ashmita'}
    return render_template('index.html', title='Home', user=user)
