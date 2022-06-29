from django.db import models
from django.contrib.auth.models import User
from research.models import Research
from validators import ValidateUser


class Researcher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)

    @staticmethod
    def create(email, username, password, first_name, last_name, phone_number):
        ValidateUser(email=email, username=username, password=password, first_name=first_name,
                     last_name=last_name, phone_number=phone_number).start_validation()
        res = Researcher(user=User.objects.create_user(email=email, username=username, password=password),
                         first_name=first_name, last_name=last_name, phone_number=phone_number)
        res.save()
        return res


class ManageResearch(models.Model):
    researcher = models.ForeignKey(Researcher, on_delete=models.SET_NULL, null=True)
    research = models.ForeignKey(Research, on_delete=models.SET_NULL, null=True)
