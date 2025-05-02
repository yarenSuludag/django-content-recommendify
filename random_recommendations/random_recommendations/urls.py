from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('recommendations.urls')),  # Ana sayfayı recommendations uygulamasına yönlendir
    path('admin/', admin.site.urls),
]
