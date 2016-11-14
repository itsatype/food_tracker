from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index_food'),
    url('new', views.new, name='new_food'),    
    url('create', views.create, name='create_food'),        
]