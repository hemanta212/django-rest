from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user_1 = User.objects.create_user(username='tempo', password='tempi')
        test_user_1.save()

        # Create a Post
        test_post = Post.objects.create(author=test_user_1, title='Hello World!', body="I am here...")
        test_post.save()
        

    def test_post_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'tempo')
        self.assertEqual(title, 'Hello World!')
        self.assertEqual(body, 'I am here...')

