from django.apps import AppConfig


class MyPortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_portfolio'

    def ready(self):
        import my_portfolio.signals
    
