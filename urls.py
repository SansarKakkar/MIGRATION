

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('index/', views.home, name='index'),  # 👈 Add this line
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('user/',views.user,name='user'),
]