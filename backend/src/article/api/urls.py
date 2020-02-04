from django.urls import path
from .views import ArticleDetailView,ArticleListview
urlpatterns=[
            path('',ArticleListview.as_view()),
            path('<pk>',ArticleDetailView.as_view())
]
