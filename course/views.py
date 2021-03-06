from course.serializers import *
from rest_framework.response import Response
from course.models import *
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView



class CourseListView(APIView):
    
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseViewSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def delete(self, request, pk ,formatn=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


