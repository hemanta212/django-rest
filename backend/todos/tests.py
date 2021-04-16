from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo', body='a body here')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_name = f'{todo.title}'
        self.assertEqual(expected_name, 'first todo')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_body = f'{todo.body}'
        self.assertEqual(expected_body, 'a body here')

