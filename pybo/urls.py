from django.urls import path
from . import views
from .views import base_views, question_views, answer_views

app_name = 'pybo'

urlpatterns = [
    #127.0.0.1:8000/pybo/
    path('', base_views.index, name='index'),
    #127.0.0.1:8000/pybo/board/
    path('board/', base_views.board, name='board'),
    #127.0.0.1:8000/pybo/1/
    path('<int:question_id>/', base_views.detail, name='detail'),


    #127.0.0.1:8000/pybo/question/create/ 질문 등록
    path('question/create/', question_views.question_create, name="question_create"),
    #질문 수정
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    #질문 삭제
    path('question/delete/<int:question_id>', question_views.question_delete, name='question_delete'),


    # 답변 등록
    path('answer/create/<int:question_id>/', answer_views.answer_create, name="answer_create"),
]