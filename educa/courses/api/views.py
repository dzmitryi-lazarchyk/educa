from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, exceptions
from rest_framework.permissions import IsAuthenticated
from .authentication import CustomAuthentication
from courses.models import Subject, Course
from courses.api.serializers import SubjectSerializer

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # lookup_field = 'title'


class CourseEnrollView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})

