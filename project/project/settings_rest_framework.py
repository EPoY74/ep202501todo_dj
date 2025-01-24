
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    
    # Настраиваю пагинацию
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE' : 10
}