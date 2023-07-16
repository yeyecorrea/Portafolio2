from django.urls import path, re_path
from . import views

app_name = 'WorkApp'

urlpatterns = [
    path('work/', views.WorkListView.as_view(), name='work'),
    path('detail-work/<int:pk>', views.WorkDetailView.as_view(), name='detail')
]