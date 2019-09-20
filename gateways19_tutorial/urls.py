from django.conf.urls import url, include

from . import views

app_name = 'gateways19_tutorial'
urlpatterns = [
    url(r'^hello/', views.hello_world, name="home"),
    url(r'^languages/', views.languages, name="languages"),
]
