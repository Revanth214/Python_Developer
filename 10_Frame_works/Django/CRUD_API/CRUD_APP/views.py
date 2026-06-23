from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


class StudentAPIView(APIView):

    # GET ALL STUDENTS
    def get(self, request):

        students = Student.objects.all()

        serializer = StudentSerializer(
            students,
            many=True
        )

        return Response(serializer.data)


    # CREATE STUDENT
    def post(self, request):

        serializer = StudentSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)
    
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


class StudentDetailAPIView(APIView):

    # UPDATE STUDENT
    def put(self, request, id):

        student = Student.objects.get(id=id)

        serializer = StudentSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)


    # DELETE STUDENT
    def delete(request, id):

        student = Student.objects.get(id=id)

        student.delete()

        return Response(
            {
                "Message": "Student deleted successfully"
            }
        )