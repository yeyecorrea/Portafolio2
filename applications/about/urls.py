from django.urls import path, re_path
from . import views

app_name = 'AboutApp'

urlpatterns = [
    path('about/', views.AboutListView.as_view(), name='about')
]