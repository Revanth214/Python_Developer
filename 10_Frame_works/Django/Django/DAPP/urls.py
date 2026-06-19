from django.urls import path
from .views import student_list, create_student

urlpatterns = [
    path("", student_list),
    path("create/", create_student),
]