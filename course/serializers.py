from rest_framework import serializers
from course.models import *

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'imgpath']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class ContactSerializer( serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['type', 'value']

class CourseSerializer(serializers.ModelSerializer):
    branches=BranchSerializer(many=True)
    contacts=ContactSerializer(many=True)
    category=CategorySerializer()

    class Meta:
        model =Course
        fields = ['id', 'name', 'description', 'logo', 'category','branches', 'contacts']
