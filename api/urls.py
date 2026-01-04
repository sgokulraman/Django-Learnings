from django.urls import path,include
from .router import Student_router
urlpatterns = [
    path("student/", include(Student_router.urls) )
]
