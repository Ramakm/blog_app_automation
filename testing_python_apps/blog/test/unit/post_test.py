from unittest import TestCase
from blog import post

class Post_Test(TestCase):
    #have to write test in first then add other things in construction
    def test_create_post(self):
        p = post('Test', 'Test Content')
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)


    def test_json_post(self):
        p = post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}
        self.assertDictEqual(expected, p.json())