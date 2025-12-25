from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index,name = 'index'),
    path("<int:question_id>/",views.details,name="details"),
    path("<int:question_id>/result/",views.results,name="results"),
    path("<int:question_id>/vote/",views.vote,name="vote"),
]
