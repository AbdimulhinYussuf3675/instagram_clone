from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.dashboard , name = 'dashboard'),
    url(r'^register/', views.register,name = 'register'),
    url(r'^login/' , auth_views.LoginView.as_view() ,name ='login'),
    url(r'^logout/' , auth_views.LogoutView.as_view(),{"next_page": '/'} ,name ='logout' ),

   
]

