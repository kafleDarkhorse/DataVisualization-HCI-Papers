from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.base, name='base'),
	url(r'^datagallery/$', views.Data_Gallery, name='Data_Gallery'),
	url(r'^about/$', views.About_page, name='About_page'),
]