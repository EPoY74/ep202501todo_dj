
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    
    'DEFAULT_AUTHENTICATION_CLASSES':[
        # 'rest_framework.authentication.TokenAuthentication',
        
        # Удалить, когда не нужен будет!!!!!
        'rest_framework.authentication.BasicAuthentication',
    ],
    
    # Разрешаю неавторизированным пользователям только чтение 
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    
    # Настраиваю пагинацию
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE' : 10
}