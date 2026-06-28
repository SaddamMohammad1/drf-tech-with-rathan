# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
# # Without serializer
# def studentsView(request):
#     # Fetch all records from the Student table
#     studetns = Student.objects.all()

#     # Convert the QuerySet into a list of dictionaries
#     # without using a Django REST Framework serializer.
#     # It's not recommended way, here using for testing purpose
#     students_list = list(studetns.values())
#     return JsonResponse(students_list, safe=False)


@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        # Get all the data from the student table
        students = Student.objects.all()
        # Using serializer to serialized the data
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # Post the data or create the data
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        # Get the single student data
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        # Update the single student data
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)