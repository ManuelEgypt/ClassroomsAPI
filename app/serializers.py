from rest_framework import serializers

from classes.models import Classroom


class ClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'year', 'teacher']


class ClassroomDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'


class UpdateClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'

class CreateClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		exclude = ['teacher']