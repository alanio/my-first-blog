from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^resume/$', views.curriculum),
    url(r'^pro/$', views.pro, name='pro'),
    url(r'^pro/en$', views.pro_en, name='pro_en'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail), 
]