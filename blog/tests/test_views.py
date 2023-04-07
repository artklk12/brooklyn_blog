from django.test import TestCase
from blog.models import Post, App


class TestSite(TestCase):

    # def test_index(self):
    #     response = self.client.get('/')
    #     self.assertEquals(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, 200)

    def test_register(self):
        response = self.client.get('/register/')
        self.assertEquals(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/logout/')
        self.assertEquals(response.status_code, 302)


class TestBlog(TestCase):

    def setUp(self):
        post = Post.objects.create(title='TestPost', author='TestAuthor', short_desc='TestShortDesc', text='TestText')
        Post.objects.create(title='TestPost2', author='TestAuthor', short_desc='TestShortDesc', text='TestText')
        Post.objects.create(title='TestPost3', author='TestAuthor', short_desc='TestShortDesc', text='TestText')
        post.tags.create(title='Machine Learning', slug='ml')
        self.post = post

    def test_blog_pagination(self):
        response = self.client.get('/blog/')
        next_page_response = self.client.get('/blog/?page=2')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(next_page_response.status_code, 200)
        self.assertIn('Читать далее', response.content.decode())
        self.assertIn('Читать далее', next_page_response.content.decode())

    def test_blog_tags(self):
        response = self.client.get('/blog/?tag=ml')
        failed_response = self.client.get('/blog/?tag=mlmlml')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(failed_response.status_code, 404)
        self.assertIn('Читать далее', response.content.decode())

    def test_post(self):
        response = self.client.get('/post/1/')
        failed_response = self.client.get('/post/1213/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(failed_response.status_code, 404)

    def test_post_hits(self):
        self.assertEquals(self.post.views_count, 0)
        self.client.get('/post/1/')
        self.assertEquals(self.post.views_count, 1)


class TestApplications(TestCase):

    def setUp(self):
        self.app = App.objects.create(title='TestApp', slug='test-app', text='TestAppText')

    def test_applications(self):
        response = self.client.get('/apps/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Подробнее', response.content.decode())

    def test_get_app(self):
        response = self.client.get('/app/test-app/')
        failed_response = self.client.get('/app/failed-app/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(failed_response.status_code, 404)
        self.assertIn('Открыть приложение', response.content.decode())

    def test_app_hits(self):
        self.assertEquals(self.app.views_count, 0)
        self.client.get('/app/test-app/')
        self.assertEquals(self.app.views_count, 1)
