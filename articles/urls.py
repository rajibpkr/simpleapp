# from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('about/',views.about ),  #first is route path and second is page
    # path('', views.homepage)     #first is route path and second is page
    path('', views.article_list, name="list"),
    # path('(?P<slug>[\w-]+)/', views.article_detail, name="detail"),
    # path('<slug:slug>/', views.article_detail, name="detail"),
]
