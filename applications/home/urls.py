from django.urls import path, re_path
from . import views

app_name = 'HomeApp'

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home')
]