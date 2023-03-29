from django.urls import path
from . import views
app_name = 'wikiTranslate'
urlpatterns = [
	path('', views.index, name= 'home'),
	path('sentences/', views.sentenceSplit, name= 'sentenceSplit'),
	path('display/(?P<pid>[0-9]+)/$', views.display, name= 'display'),
	path('projects/', views.project_list, name='project_list'),
]