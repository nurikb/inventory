command = '/home/nurik/Desktop/dj/inventory/bin/gunicorn'
pythonpath = '/home/nurik/Desktop/dj/app/inventoryengine'
bind = '127.0.0.1:8001'
workers = 5
user = 'nurik'
limit_request_fields = 32000
limit_request_fields_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=inventoryengine.settings'


