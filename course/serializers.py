from rest_framework import serializers
from course.models import *

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'imgpath']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['latitude', 'longitude', 'address']

class ContactSerializer( serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['type', 'value']

class CourseViewSerializer(serializers.ModelSerializer):
    branches=BranchSerializer(many=True)
    contacts=ContactSerializer(many=True)
    category=CategorySerializer()
    
    class Meta:
        model =Course
        fields = ['id', 'name', 'description', 'logo', 'category','branches', 'contacts']

class CourseSerializer(serializers.ModelSerializer):
    branches=BranchSerializer(many=True)
    contacts=ContactSerializer(many=True)

    class Meta:
        model =Course
        fields = ['id', 'name', 'description', 'logo', 'category','branches', 'contacts']
        
    def create(self, validated_data):
       contacts_data = validated_data.pop('contacts')
       branches_data = validated_data.pop('branches')
       course = Course.objects.create(**validated_data)

       for contact_data in contacts_data:
           Contact.objects.create(course=course, **contact_data)

       for branch_data in branches_data:
           Branch.objects.create(course=course, **branch_data)
       return course

