from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from .views import Student_view,Student_problem_view,Leader_View



Student_Router = DefaultRouter()
Student_Router.register(r"detail",Student_view)
Student_Router.register(r"problem",Student_problem_view)


Leader_Router = DefaultRouter()
Leader_Router.register(r"access",Leader_View)