from django.conf.urls import url, include
from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.home, name="home_page"),
    url(r'^query/$', views.query, name="query")
]
