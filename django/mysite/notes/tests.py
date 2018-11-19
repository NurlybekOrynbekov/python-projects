from django.test import TestCase
from .models import Note

class NoteTestCase(TestCase):
    def test_create_without_author(self):
        note = Note.objects.create(
            title='Without Author',
            body='Some body text for note without author')
        self.assertEqual(note.author, 'anonymous')



    def test_create_with_author(self):
        note = Note.objects.create(
            title='With Author', 
            body='Some body text for note with author', 
            author='Nurik')
        self.assertEqual(note.author, 'Nurik')