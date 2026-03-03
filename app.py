import os
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
            <br>
            <a href="#" class="boton">¡Funciona perfectamente!</a>
        </body>
    </html>
    """

# 3. ESTA ES LA PARTE MÁS IMPORTANTE PARA RAILWAY
# Sin esto, la web se "estrella" porque no encuentra el puerto
if _name_ == "_main_":
    # Railway nos da un puerto dinámico, aquí lo capturamos
    port = int(os.environ.get("PORT", 8080))
    # '0.0.0.0' permite que la web sea visible desde el exterior
    app.run(host='0.0.0.0', port=port)
