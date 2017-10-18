from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^from', views.from_warsaw),
    url(r'^to', views.to_warsaw),
    url(r'^run/working', views.working_day),
    url(r'^run/saturday', views.saturday),
    url(r'^run/sunday', views.sunday),
]