from django.contrib import admin
from django.urls import path, include 
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('about/',views.about ),  #first is route path and second is page
    path('', views.homepage),    #first is route path and second is page
    
]

urlpatterns += staticfiles_urlpatterns()