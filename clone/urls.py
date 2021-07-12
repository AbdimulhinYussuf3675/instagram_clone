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
    url(r'^edit/', views.edit, name='edit'),
    url(r'^create/', views.create, name='create'),
    url(r'^profile/', views.profile, name= 'profile'),
    url(r'^profile/<username>', views.get_profile, name= 'get_profile'),
    url(r'^comment/<int:pk>', views.comment , name= 'comment'),
    url(r'^follow/<int:user_to>', views.follow , name= 'follow'),
    url(r'^like/', views.like , name= 'like'),
    url(r'^searches/' , views.searches , name = 'searches')
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

