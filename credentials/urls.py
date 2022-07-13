from. import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('user/',views.user,name='user'),
    path('accform/',views.accform,name='accform'),
    path('message',views.message,name='message'),
]