from ast import Pass
from django.test import TestCase
from user.models import User
from argon2 import PasswordHasher

class UserTest(TestCase):

    def test_user_validation(self):
        user = User( 
            email = "ldy9037@naver.com", 
            name = "이동열", 
            nickname="hani_6_6", 
            phone_number="010-5264-5565",
            password=PasswordHasher().hash("!@#ldy12345")
        )
        self.assertEqual(user.email, "ldy9037@naver.com")
        self.assertEqual(user.name, "이동열")
        self.assertEqual(user.nickname, "hani_6_6")
        self.assertEqual(user.phone_number, '010-5264-5565')
        self.assertTrue(PasswordHasher().verify(user.password, '!@#ldy12345'))
        user.full_clean()
            