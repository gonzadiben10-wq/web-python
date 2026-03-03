[17:04, 3/3/2026] .: import os
from flask import Flask

# 1. Configuración de la aplicación
app = Flask(_name_)

# 2. Tu contenido (Aquí es donde ocurre la magia)
@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Mi Web en Railway</title>
            <style>
                body { font-family: sans-serif; text-align: center; padding: 50px; background-color: #f4f4f4; }
                h1 { color: #333; }
                p { color: #666; }
                .boton { background: #007bff; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; }
            </style>
        </head>
        <body>
            <h1>¡Mi Web ya está Viva! 🚀</h1>
            <p>He configurado correctamente el puerto y ahora Railway funciona.</p>
  …
[17:20, 3/3/2026] .: import os
from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Mi Web Gratis</title>
            <style>
                body { font-family: Arial; text-align: center; background: #2c3e50; color: white; padding-top: 100px; }
                .card { background: #34495e; display: inline-block; padding: 40px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.3); }
                h1 { color: #2ecc71; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>¡Web Online con Railway! 🚀</h1>
                <p>El servidor está funcionando correctamente.</p>
                <p>Estado: <b>Activo</b></p>
            </div>
        </body>
    </html>
    """

if _name_ == "_main_":
   
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
