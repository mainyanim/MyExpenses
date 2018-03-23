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
    path('exp/<int:pk>/delete/', views.ExpDelete.as_view(), name='expenses_confirm_delete'),
    url(r'^exp/(?P<pk>\d+)/exp/$', views.add_note_to_post, name='add_note_to_post'),

]