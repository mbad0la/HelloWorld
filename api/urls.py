from django.conf.urls import url,handler404
from django.conf import settings
from . import views

# handler404 = 'views.handler404'

urlpatterns=[
	url(r'^projects/$',views.projects,name='projects'),
	url(r'^projects/(?P<project_slug>[\w-]+)/$',views.project_details,name='project_detail'),
	url(r'^members/$',views.members,name="members"),
]
