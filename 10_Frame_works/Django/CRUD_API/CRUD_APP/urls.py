from django.urls import path

from .views import (
    StudentAPIView,
    StudentDetailAPIView
)

urlpatterns = [

    path(
        "students/",
        StudentAPIView.as_view()
    ),

    path(
        "students/<int:id>/",
        StudentDetailAPIView.as_view()
    ),

]