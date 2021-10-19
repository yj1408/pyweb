from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    #127.0.0.1:8000/pybo/
    path('', views.index, name='index'),
    #127.0.0.1:8000/pybo/board/
    path('board/', views.board, name='board'),
    #127.0.0.1:8000/pybo/1/
    path('<int:question_id>/', views.detail, name='detail'),
    #127.0.0.1:8000/pybo/question/create/ 질문 등록
    path('question/create/', views.question_create, name="question_create"),
    # 답변 등록
    path('answer/create/<int:question_id>/', views.answer_create, name="answer_create"),
    #질문 수정
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    #질문 삭제
    path('question/delete/<int:question_id>', views.question_delete, name='question_delete'),
]