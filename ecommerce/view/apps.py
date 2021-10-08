from django.apps import AppConfig

#creating an app for the view app
class ViewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'view'
