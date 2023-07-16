from django.urls import path, re_path
from . import views

app_name = 'BlogApp'

urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('blog-detail/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail')
]