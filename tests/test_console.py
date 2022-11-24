#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
import json
import pep8
import console
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os
import sys


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'file')
def test_create_good(self):
        """ Test the create function """
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(help_val.getvalue()) > 0)