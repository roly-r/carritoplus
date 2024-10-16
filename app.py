from flask import Flask, render_template,request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'unaclavesecreta'

@app.route("/")
def index():
    if 'carrito' not in session:
        session['carrito'] = []
    total = sum(item['precio']*item['cantidad'] for item in session['carrito'])
    return render_template('index.html', carrito = session['carrito'], total = total)

@app.route("/procesa", methods = ['POST'])
def procesa():
    producto = request.form.get('producto')
    precio = float(request.form.get('precio'))
    cantidad = int(request.form.get('cantidad'))

    if 'carrito' not in session:
        session['carrito'] = []
    
    session['carrito'].append({'producto':producto, 'precio':precio, 'cantidad':cantidad })
    session.modified = True
    return redirect(url_for("index"))

@app.route("/vaciar")
def vaciar():
    session.pop('carrito', None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)