from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:    #중첩 클래스(내부 클래스)
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '질문 내용'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {'content': '답변 내용'}