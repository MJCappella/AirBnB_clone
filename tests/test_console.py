#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import os

class TestConsole(unittest.TestCase):
    def setUp(self):
        """Sets up the console and redirects stdout to a StringIO object."""
        self.console = HBNBCommand()
        self.stdout = StringIO()

    def tearDown(self):
        """Cleans up after each test by resetting sys.stdout."""
        self.stdout.close()

    def test_create(self):
        """Test the create command."""
        with patch('sys.stdout', new=self.stdout):
            self.console.onecmd("create BaseModel")
            output = self.stdout.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_show(self):
        """Test the show command."""
        with patch('sys.stdout', new=self.stdout):
            self.console.onecmd("create BaseModel")
            obj_id = self.stdout.getvalue().strip()
            self.stdout = StringIO()  # Reset stdout
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = self.stdout.getvalue().strip()
            self.assertIn(obj_id, output)

    def test_update(self):
        """Test the update command."""
        with patch('sys.stdout', new=self.stdout):
            self.console.onecmd("create BaseModel")
            obj_id = self.stdout.getvalue().strip()
            self.stdout = StringIO()  # Reset stdout
            self.console.onecmd(f"update BaseModel {obj_id} name 'new_name'")
            updated_obj_id = f"BaseModel.{obj_id}"
            updated_obj = self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertIn("new_name", updated_obj)

    def test_destroy(self):
        """Test the destroy command."""
        with patch('sys.stdout', new=self.stdout):
            self.console.onecmd("create BaseModel")
            obj_id = self.stdout.getvalue().strip()
            self.stdout = StringIO()  # Reset stdout
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = self.stdout.getvalue().strip()
            self.assertIn("** no instance found **", output)

if __name__ == '__main__':
    unittest.main()
