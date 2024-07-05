# settings.py

INSTALLED_APPS = [
    
    'usuarios', 
    
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = 'home'  
LOGOUT_REDIRECT_URL = 'login' 
