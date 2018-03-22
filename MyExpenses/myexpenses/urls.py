from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

]

urlpatterns = [
    url(r'^$', views.exp_list, name='exp_list'),
    url(r'^exp/(?P<pk>\d+)/$', views.exp_detail, name='exp_detail'),
    url(r'^exp/new/$', views.exp_new, name='exp_new'),
    url(r'^exp/(?P<pk>\d+)/edit/$', views.exp_edit, name='exp_edit'),
    url(r'^exp/(?P<pk>\d+)/delete/$', views.exp_delete, name='exp_delete'),

]