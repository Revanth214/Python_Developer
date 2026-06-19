from django.shortcuts import render, redirect

# Create your views here.

# from django.http import HttpResponse

# def fun(request):
#     return HttpResponse("Drums of Liberation")

# from .forms import Classic

# def class_form(request):
#     ab=Classic()
#     return render(request, "login.html", {'forms':ab})

# def get_post(request):
#     if request.method == "POST":
#         user=request.POST["username"]
#         passw=request.POST["password"]
#         return render(request, "msg.html", {'usern': user})
#     else:
#         return render(request, "admin.html")
    
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


@api_view(["GET"])
def student_list(request):

    students = Student.objects.all()

    serializer = StudentSerializer(
        students,
        many=True
    )

    return Response(serializer.data)
# Why @api_view : 

# ✅ Creates a DRF API View

# ✅ Restricts allowed methods

# ✅ Prepares renderers

# ✅ Prepares request parsing

# ✅ Makes Response() work

# Exact flow : 

# Browser
#    ↓
# /api/students/
#    ↓
# urls.py
#    ↓
# student_list()
#    ↓
# Student.objects.all()
#    ↓
# QuerySet
#    ↓
# StudentSerializer()
#    ↓
# serializer.data
#    ↓
# Response()
#    ↓
# JSON
#    ↓
# Client

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StudentSerializer


@api_view(["POST"])
def create_student(request):

    serializer = StudentSerializer(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(
            {
                "message": "Student created successfully",
                "data": serializer.data
            }
        )

    return Response(
        {
            "errors": serializer.errors
        }
    )


@api_view(["PUT"])
def update_student(request, id):

    student = Student.objects.get(id=id)

    serializer = StudentSerializer(
        student,
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)




@api_view(["DELETE"])
def delete_student(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return Response(
        {
            "Message": "Student deleted successfully"
        }
    )