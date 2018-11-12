from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^people/', views.people, name="people"),
    url(r'^$', views.people, name="people"),
]
