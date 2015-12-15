from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^blog/historia/$',views.historia),
    url(r'^blog/myv/$',views.myv),
    url(r'^blog/departamentos/$',views.departamentos),
    url(r'^blog/anatomia/$',views.anatomia),
    url(r'^blog/biologia/$',views.biologia),
    url(r'^blog/bioquimica/$',views.bioquimica),
    url(r'^blog/cirugia/$',views.cirugia),
    url(r'^blog/embriologia/$',views.embriologia),
    url(r'^blog/farmacologia/$',views.farmacologia),
    url(r'^blog/fisiologia/$',views.fisiologia),
    url(r'^blog/filosofia/$',views.filosofia),
    url(r'^blog/informatica/$',views.informatica),
    url(r'^blog/ciencias/$',views.ciencias),
    url(r'^blog/microbiologia/$',views.microbiologia),
    url(r'^blog/psiquiatria/$',views.psiquiatria),
]