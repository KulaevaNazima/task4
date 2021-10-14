from django.test import TestCase

from course.models import *

class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='it', imgpath='it')
        Course.objects.create(name='Python', description='Python course', category_id=1, logo='logo')

    def test_name_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_logo_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('logo').verbose_name
        self.assertEqual(field_label, 'logo')

    def test_name_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)
    
    def test_logo_label(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('logo').max_length
        self.assertEqual(max_length, 255)

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='it', imgpath='it')
        Course.objects.create(name='Python', description='Python course', category_id=1, logo='logo')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_imgpath_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('imgpath').verbose_name
        self.assertEqual(field_label, 'imgpath')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)
    
    def test_imgpath_label(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('imgpath').max_length
        self.assertEqual(max_length, 255)

class BranchModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='it', imgpath='it')
        Course.objects.create(name='Python', description='Python course', category_id=1, logo='logo')
        Branch.objects.create(latitude='test', longitude='test', address='test', course_id=1)

    def test_latitude_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field('latitude').verbose_name
        self.assertEqual(field_label, 'latitude')

    def test_longitude_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field('longitude').verbose_name
        self.assertEqual(field_label, 'longitude')

    def test_address_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_latitude_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('latitude').max_length
        self.assertEqual(max_length, 255)
    
    def test_longitude_label(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('longitude').max_length
        self.assertEqual(max_length, 255)

    def test_address_label(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('address').max_length
        self.assertEqual(max_length, 255)

class ContactModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='it', imgpath='it')
        Course.objects.create(name='Python', description='Python course', category_id=1, logo='logo')
        Contact.objects.create(type='1', value='0555858585', course_id=1)

    def test_value_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('value').verbose_name
        self.assertEqual(field_label, 'value')

    def test_value_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('value').max_length
        self.assertEqual(max_length, 255)
    



