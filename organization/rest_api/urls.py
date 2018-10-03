from django.urls import path
from . import views

app_name = 'rest_api'
urlpatterns = [
    path('api/words', views.words, name='words'),
    path('api/words/<int:word_id>', views.words, name='words'),
    path('api/<int:word_id>/video', views.video, name='video'),
]
