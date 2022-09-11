""" Import AppConfig"""
from django.apps import AppConfig


class BaseConfig(AppConfig):
    """ Base class for app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
