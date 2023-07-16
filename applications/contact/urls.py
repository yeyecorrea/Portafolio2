from django.urls import path, re_path
from . import views

app_name = 'ContactApp'

urlpatterns = [
    path('contact/', views.Contact.as_view(), name='contact')
]