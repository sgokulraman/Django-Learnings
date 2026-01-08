from django.urls import path, include
from .router import Student_Router, Leader_Router
urlpatterns = [
    path("student/", include(Student_Router.urls)),
    path("leader/",include(Leader_Router.urls))
]
