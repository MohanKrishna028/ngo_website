from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('donate/', views.donate, name="donate"),
    path('volunteer/', views.volunteer, name="volunteer"),
    path('contact/', views.contact, name="contact"),
]
