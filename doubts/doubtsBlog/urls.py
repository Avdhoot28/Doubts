from django.urls import path
from .views import (
    DoubtListView,
    DoubtDetailView,
    DoubtCreateView,
    AnswerCreateView,
    DoubtDeleteView,
    AnswerDeleteView,
    AuthorDetailView
)
from . import views

urlpatterns = [
	path('', DoubtListView.as_view(), name='doubtsBlog-home'),
	path('doubt/<int:pk>/', DoubtDetailView.as_view(), name='doubt-detail'),
	path('doubt/new/', DoubtCreateView.as_view(), name='doubt-create'),
	path('doubt/<int:pk>/answer/new/', AnswerCreateView.as_view(), name='answer-create'),
	path('doubt/<int:pk>/delete/', DoubtDeleteView.as_view(), name='doubt-delete'),
	path('answer/<int:pk>/delete/', AnswerDeleteView.as_view(), name='answer-delete'),
	path('answer/<int:pk>/vote/', AuthorDetailView.as_view(), name='answer-vote'),
]