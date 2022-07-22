from django.urls import path
from sport_news.views import index
from . import views

app_name = 'users'
urlpatterns = [
    #login page
    path('login/home/',index,name='index'),
    path('login/',views.loginview,name='login'),
    path('logout/',views.logooutview,name='logout'),
    path('register/',views.register,name='register')
]