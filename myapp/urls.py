
from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service_view, name='service_view'),
    # path('home/', views.home, name='home'),  # Добавляем URL для home
    path('success/', views.success_page, name='success_page'),
]