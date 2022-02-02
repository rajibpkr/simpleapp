# from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('about/',views.about ),  #first is route path and second is page
    # path('', views.homepage)     #first is route path and second is page
    path('', views.article_list, name="list"),
    # path('', views.article_list),
    # path('(?P<slug>[\w-]+)/', views.article_detail),
    # path('articles/slug', views.article_detail, name="detail"),
    # path('(?P<slug>[\w-]+)/', views.article_detail, name="detail"),
    # path('<slug:slug>/', views.article_detail, name="detail"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

