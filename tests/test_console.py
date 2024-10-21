import unittest
from io import StringIO
from unittest.mock import patch
import sys
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Prepare the test environment."""
        self.console = HBNBCommand()
        self.console.prompt = '(hbnb) '

    def tearDown(self):
        """Clean up after tests."""
        storage.all().clear()  # Assuming storage.all() returns a dictionary of instances

    def test_prompt(self):
        """Test prompt initialization."""
        self.assertEqual(self.console.prompt, '(hbnb) ')

    def test_do_quit(self):
        """Test the quit command."""
        self.assertTrue(self.console.do_quit(""))

    def test_do_EOF(self):
        """Test the EOF command."""
        with self.assertRaises(SystemExit):
            self.console.do_EOF("")  # This should raise SystemExit

    def test_do_create(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_create("BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(output)  # Expect an ID to be printed

    def test_do_show(self):
        """Test the show command."""
        bm = BaseModel()
        bm.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_show(f"BaseModel {bm.id}")
            output = fake_out.getvalue().strip()
            self.assertIn(bm.id, output)

    def test_do_destroy(self):
        """Test the destroy command."""
        bm = BaseModel()
        bm.save()
        self.console.do_destroy(f"BaseModel {bm.id}")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_show(f"BaseModel {bm.id}")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_all(self):
        """Test the all command."""
        bm1 = BaseModel()
        bm1.save()
        bm2 = BaseModel()
        bm2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_all("")
            output = fake_out.getvalue().strip()
            self.assertIn(bm1.id, output)
            self.assertIn(bm2.id, output)

    def test_do_count(self):
        """Test the count command."""
        bm1 = BaseModel()
        bm1.save()
        bm2 = BaseModel()
        bm2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_count("BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "2")  # Expecting count of 2

    def test_do_update(self):
        """Test the update command."""
        bm = BaseModel()
        bm.save()
        self.console.do_update(f"BaseModel {bm.id} name 'New Name'")
        # above line has an f-string. will it work?

        # Check if the attribute was updated correctly
        self.assertTrue(hasattr(bm, 'name'))  # Check if name attribute exists
        self.assertEqual(bm.name, 'New Name')  # Verify the value is updated


if __name__ == '__main__':
    unittest.main()
