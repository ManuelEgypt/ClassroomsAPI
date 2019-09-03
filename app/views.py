from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from datetime import datetime

from classes.models import Classroom
from .serializers import ClassroomSerializer, ClassroomDetailsSerializer, UpdateClassroomSerializer, CreateClassroomSerializer

# Create your views here.

class ClassroomsList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer

class ClassroomDetails(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class UpdateClassroom(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UpdateClassroomSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'



class CancelClassroom(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class CreateClassroom(CreateAPIView):
	serializer_class = CreateClassroomSerializer

	def perform_create(self,serializer):
		serializer.save(teacher=self.request.user)
