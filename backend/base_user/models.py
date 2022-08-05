from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from .validators import ValidateBaseUser


class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()

    @staticmethod
    def create(email, username, password, first_name, last_name, phone_number):
        ValidateBaseUser(email=email, username=username, password=password, first_name=first_name,
                         last_name=last_name, phone_number=phone_number).start_validation()

        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(raw_password=password)
        user.save()

        base_user = BaseUser(user=user, phone_number=phone_number)
        base_user.save()

        return base_user

    def update_data(self, data):
        if 'email' in data.keys():
            self.user.email = data['email']
        if 'username' in data.keys():
            self.user.username = data['username']
        if 'password' in data.keys():
            self.user.set_password(data['password'])
        if 'first_name' in data.keys():
            self.user.first_name = data['first_name']
        if 'last_name' in data.keys():
            self.user.last_name = data['last_name']
        if 'phone_number' in data.keys():
            self.phone_number = data['phone_number']
        self.user.save()
        self.save()
