from django.apps import AppConfig


class EmailSetConfig(AppConfig):
    name = 'email_set'
  
    def ready(self):
        import email_set.signals