from django.contrib.auth.urls import views as auth_views
from django.conf.urls import url
from accounts import views


app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name= 'accounts/logout'), name= 'logout'),
    
]
