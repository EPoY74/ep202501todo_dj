
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    
    # определяю, какие классы аутентификации будут использоваться
    'DEFAULT_AUTHENTICATION_CLASSES':[
        
        # Аутентификация по токену
        'rest_framework.authentication.TokenAuthentication',
        
        # Аутертификация по сессии
        'rest_framework.authentication.SessionAuthentication',
        
        # Аутентификация jwt
        'rest_framework_simplejwt.authentication.JWTAuthentication',
            
        # Удалить, когда не нужен будет!!!!!
        # 'rest_framework.authentication.BasicAuthentication',
    ],
    
    # Какие разрешения будут по умолчанию
    # Разрешаю неавторизированным пользователям только чтение 
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    
    # Настраиваю пагинацию
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE' : 10
}