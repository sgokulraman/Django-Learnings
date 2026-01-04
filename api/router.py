from rest_framework.routers import DefaultRouter
from .views import Api_router

Student_router = DefaultRouter()
Student_router.register(r"student",Api_router)