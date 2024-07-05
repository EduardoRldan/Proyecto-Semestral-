# settings.py

INSTALLED_APPS = [
    ...
    'usuarios',  # Asegúrate de que tu aplicación esté registrada aquí
    ...
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = 'home'  # Redirige al usuario a la página de inicio después del inicio de sesión
LOGOUT_REDIRECT_URL = 'login'  # Redirige al usuario a la página de inicio de sesión después de cerrar sesión
