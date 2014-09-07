import unittest
import console_application
import extention
import menu
import os
from time import strftime


class TestCreatingNote(unittest.TestCase):

    """Tests if there is file with note's name"""

    def test_note_file_created(self):
        note = console_application.Note()
        current_directory_files = [
            file_ for file_ in os.listdir('.') if os.path.isfile(file_)]
        self.assertTrue(note.name in current_directory_files)


class TestCreatingTODO(unittest.TestCase):

    """Tests if there is file with TODO's name"""

    def test_todo_file_created(self):
        todo = console_application.TODO()
        current_directory_files = [
            file_ for file_ in os.listdir('.') if os.path.isfile(file_)]
        self.assertTrue(todo.name in current_directory_files)


class TestCreatingSubject(unittest.TestCase):

    """Tests if there is file with note's name"""

    def test_subject_file_created(self):
        subject = extention.Subject()
        current_directory_files = [
            file_ for file_ in os.listdir('.') if os.path.isfile(file_)]
        self.assertTrue(subject.name in current_directory_files)


def simulate_text():
    return "Some text here."


class TestNoteText(unittest.TestCase):

    """Tests if note's text is what is given"""

    def test_note_text(self):
        note = console_application.Note()
        note.add(simulate_text)
        self.assertEqual(note.text, "Some text here.")


class TestTODOText(unittest.TestCase):

    """Tests if TODO's text is what is given"""

    def test_todo_text(self):
        todo = console_application.TODO()
        todo.add(simulate_text)
        self.assertEqual(todo.text, "Some text here.")


class TestSubjectText(unittest.TestCase):

    """Tests if subject's text is what is given"""

    def test_subject_text(self):
        subject = extention.Subject()
        subject.add(simulate_text)
        self.assertEqual(subject.text, "Some text here.")


class TestTODOStartDate(unittest.TestCase):

    """Tests if TODO's start date is accurate"""

    def test_start_date(self):
        todo = console_application.TODO()
        self.assertEqual(todo.start_date, strftime("%Y-%m-%d_%H:%M:%S")[:10])


class TestTODOFinnished(unittest.TestCase):

    def test_not_finnished(self):
        todo = console_application.TODO()
        self.assertTrue(not todo.is_finished)


class TestTODONoFinnishDate(unittest.TestCase):

    """Test no string for finnish date"""

    def test_no_finnish_date(self):
        todo = console_application.TODO()
        self.assertEqual(todo.finish_date, '')

if __name__ == '__main__':
    unittest.main()
