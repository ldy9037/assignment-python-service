from django.core.exceptions import ValidationError
from django.test import TestCase
from user_service import validators
import re

class UserTest(TestCase):

    def test_name_validator(self):
        validators.validate_name("이동열")
        validators.validate_name("ldy")

        with self.assertRaises(ValidationError):
            validators.validate_name("이동열!")

        with self.assertRaises(ValidationError):
            validators.validate_name("ldy!")
        
    def test_phone_number_validator(self):
        validators.validate_phone_number("010-5264-5565")
        validators.validate_phone_number("010-564-5625")

        with self.assertRaises(ValidationError):
            validators.validate_phone_number("01052645565")
    
    def test_password_validator(self):
        validators.validate_password("!@#hdwdduf1234")
        
        with self.assertRaises(ValidationError):
            validators.validate_password("123455677")

        with self.assertRaises(ValidationError):
            validators.validate_password("!We21")