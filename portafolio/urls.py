from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
    path('about-app/', include('applications.about.urls')),
    path('work-app/', include('applications.work.urls')),
    path('blog-app/', include('applications.blog.urls')),
    path('contact-app/', include('applications.contact.urls'))
]
