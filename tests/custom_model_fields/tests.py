from django.db import models
from django.test import SimpleTestCase
from django.test.utils import isolate_apps

from .fields import NulledCharField


class CustomModelFieldTests(SimpleTestCase):
    def assertSQLEqual(self, qs1, qs2):
        self.assertEqual(str(qs1.query), str(qs2.query))

    @isolate_apps('custom_model_fields')
    def test_nulledcharfield(self):
        """
        If a custom model field has a `get_prep_value` that attempts to convert a value to None,
        we must ensure this is handled the same way as it would've been if it was None off the bat.
        """
        class Book(models.Model):
            # Example usage of NulledCharField: Serial may be set or not, but when it is, must be unique.
            serial = NulledCharField(max_length=128, unique=True, blank=True, null=True)

        self.assertSQLEqual(Book.objects.filter(serial=''), Book.objects.filter(serial=None))
        self.assertSQLEqual(Book.objects.exclude(serial=''), Book.objects.exclude(serial=None))
