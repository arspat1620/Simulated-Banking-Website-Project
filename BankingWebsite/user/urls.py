from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.loginV,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutV,name='logout')
]
