from page import create_app

# Crea una instancia de la aplicación Flask utilizando la función create_app
app = create_app()

# Ejecuta la aplicación Flask si este script se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo de depuración

