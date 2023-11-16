from django.test import TestCase

class Test(TestCase):
    def test_something(self):
        self.assertEqual(True, True)

'''
python manage.py test main.tests.Test.test_something_a
'''