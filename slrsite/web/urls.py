from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('about',views.About,name='about'),
    path('team',views.Team,name='team'),
    path('ai',views.Ai,name='ai'),
    path('search',views.Search,name='search'),
    path('voice',views.Voice,name='voice'),
    path('action',views.Action,name='action'),
    path('stream', views.video_stream, name='stream'),
    path('ai/',views.get_data,name='get_data')
]