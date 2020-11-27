from unittest import TestCase
from blog import Blog

class blog_Test(TestCase):
    #have to write test in first then add other things in construction
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([],b.posts)

