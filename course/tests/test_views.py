from django.test import TestCase
from django.urls import reverse

from course.models import Category, Course

class CourseListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='it', imgpath='it')
        Course.objects.create(name='Python', description='Python course', category_id=1, logo='logo')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)




