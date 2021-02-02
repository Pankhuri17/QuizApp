from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url



urlpatterns = [  
    path('', home , name="home"),
    path('view_score' , view_score , name="view_score"),
    path('api/check_score' , check_score , name="check_score"),
    path('<id>' , take_quiz, name="take_quiz"),
    path('api/<id>', api_question, name= "api_question"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
