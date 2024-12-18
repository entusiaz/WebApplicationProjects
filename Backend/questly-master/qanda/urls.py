from django.urls.conf import path
from django.urls import path

from qanda import views
from . import views


app_name = 'qanda'
urlpatterns = [
    path('', views.index, name='index'),
    path('ask', views.AskQuestionView.as_view(), name='ask'),
    path('q/<int:pk>', views.QuestionDetailView.as_view(), name='question_detail'),
    path('q/<int:pk>/answer', views.CreateAnswerView.as_view(),
         name='answer_question'),
    path('a/<int:pk>/accept', views.UpdateAnswerAcceptance.as_view(),
         name='update_answer_acceptance'),
    path('daily/<int:year>/<int:month>/<int:day>/',
         views.DailyQuestionList.as_view(), name='daily_questions'),
]
