from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('sent',views.sentence,name='sentence'),
    path('gettweet',views.get_tweets,name='tweets')
]
