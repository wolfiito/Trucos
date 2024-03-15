from flask import Flask, render_template
from app.carrusel.carrusel import carrusel_bp

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('nav.html')
app.register_blueprint(carrusel_bp)
    
if __name__ == '__main__':
    app.run(debug=True)