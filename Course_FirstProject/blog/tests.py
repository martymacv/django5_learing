from django.test import SimpleTestCase


class HomePageGetTests(SimpleTestCase):
    def test_url_access(self):
        url = '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class AboutPageGetTests(SimpleTestCase):
    def test_url_access(self):
        url = '/about/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ContactPageGetTests(SimpleTestCase):
    def test_url_access(self):
        url = '/contact/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)