from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('user/index.html')

@app.route('/about')
def about():
    return render_template('user/about.html')

@app.route('/services')
def services():
    return render_template('user/services.html')

@app.route('/products')
def products():
    return render_template('user/products.html')

@app.route('/testimonials')
def testimonials():
    return render_template('user/testimonials.html')

@app.route('/contact')
def contact():
    
    return render_template('user/contact.html')

@app.route('/about_rohit')
def about_rohit():
    return render_template('user/about_rohit.html')

if __name__ == '__main__':
    app.run(debug=True)
