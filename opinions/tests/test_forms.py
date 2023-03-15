from django.test import SimpleTestCase
from opinions.forms import OpinionForm

class TestForms(SimpleTestCase):

    def test_opinion_form_is_valid(self):
        form = OpinionForm(data={
            'topic': 'topic',
            'rating': 3,
            'message': 'Hello little seal'
        })

        self.assertTrue(form.is_valid())

    def test_opinion_form_no_data(self):
        form = OpinionForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
