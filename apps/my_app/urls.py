from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^contact$', views.contact),
    url(r'^records$', views.records),
    url(r'^check$', views.check),
    url(r'^admin$', views.admin),
    url(r'^activate/(?P<id>\d+)$', views.activate),
    url(r'^deactivate/(?P<id>\d+)$', views.deactivate),
    

]