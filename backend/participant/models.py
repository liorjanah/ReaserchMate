from django.db import models
from django.contrib.auth.models import User
from validators import ValidateUser


class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)

    @staticmethod
    def create(email, username, password, first_name, last_name, phone_number):
        ValidateUser(email=email, username=username, password=password, first_name=first_name,
                     last_name=last_name, phone_number=phone_number).start_validation()
        res = Participant(user=User.objects.create_user(email=email, username=username, password=password),
                          first_name=first_name, last_name=last_name, phone_number=phone_number)
        res.save()
        return res

    @staticmethod
    def get_by_id(participant_id):
        result = Participant.objects.filter(id=participant_id).first()
        return result

    @staticmethod
    def get_all():
        return Participant.objects.all()
