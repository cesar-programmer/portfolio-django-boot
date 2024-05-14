from django.urls import path
from .views import TestView, AboutView, ContactView

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('testing/', TestView.as_view(), name='test'),
    path('contact/', ContactView.as_view(), name='contact'),
]
