from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    #127.0.0.1:8000/poll/poll_list
    path('poll_list/', views.poll_list, name="poll_list"),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/result/', views.result, name='result'),
]