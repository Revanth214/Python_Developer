from django.urls import path
from .views import student_list, create_student, update_student, delete_student

urlpatterns = [
    path("", student_list),
    path("create/", create_student),
    path("update/<int:id>/", update_student),
    path("delete/<int:id>/", delete_student),
]