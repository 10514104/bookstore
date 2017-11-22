from django.conf.urls import url
from main import views


urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^contact/$', views.contact, name='contact'),
]