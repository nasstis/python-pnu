from flask import url_for
from .base import BaseTest

class PortfolioTest(BaseTest):
    def test_view_index(self):
        with self.client:
            response = self.client.get(url_for('portfolio.index'))

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Hello!', response.data)

    def test_view_about(self):
        with self.client:
            response = self.client.get(url_for('portfolio.about'))

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Tsapko Anastasiia', response.data)

    def test_view_contact(self):
        with self.client:
            response = self.client.get(url_for('portfolio.contact'))

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Contacts', response.data)

    def test_view_skills(self):
        with self.client:
            response = self.client.get(url_for('portfolio.skill'))

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Python', response.data)
            self.assertIn(b'Flutter', response.data)