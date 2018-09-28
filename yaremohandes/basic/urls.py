from django.conf.urls import url
from basic import views



urlpatterns = [
    url(r'^about/$', views.About.as_view(), name='about'),
    url(r'^software/$', views.Software.as_view(), name='software'),
    url(r'^contact/$', views.Contact, name='contact'),
    url(r'^MyProfile/$', views.MyProfile.as_view(), name='MyProfile'),
    url(r'^teaching/$', views.Teaching.as_view(), name='teaching'),

]
