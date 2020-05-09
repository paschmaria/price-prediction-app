from django.apps import AppConfig


class MLAppConfig(AppConfig):
    name = 'ml_app'
    verbose_name = 'ML App'

    def ready(self):
        import ml_app.signals
