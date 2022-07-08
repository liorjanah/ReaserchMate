from django.db import models
from .validators import ValidateResearch, ValidateResearchField
from django.core.exceptions import ObjectDoesNotExist
from participant.models import Participant
from django.utils import timezone


class ResearchField(models.Model):
    name = models.CharField(max_length=255)

    @staticmethod
    def create(name):
        ValidateResearchField(name).start_validation()
        res = ResearchField(name=name)
        res.save()
        return res

    @staticmethod
    def is_name_exist(name):
        try:
            result = ResearchField.objects.filter(name=name)
            if len(result) > 0:
                return True
            return False
        except ObjectDoesNotExist:
            return False

    @staticmethod
    def get_field_by_id(filed_id):
        result = ResearchField.objects.filter(id=filed_id).first()
        return result


class Research(models.Model):
    name = models.CharField(max_length=255)
    field = models.ForeignKey(ResearchField, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField()

    @staticmethod
    def create(name, field_id, capacity):
        ValidateResearch(name).start_validation()
        field = ResearchField.get_field_by_id(filed_id=field_id)
        res = Research(name=name, field=field, capacity=capacity)
        res.save()
        return res

    @staticmethod
    def is_research_name_exist(name):
        try:
            result = Research.objects.filter(name=name)
            if len(result) > 0:
                return True
            return False
        except ObjectDoesNotExist:
            return False

    @staticmethod
    def is_research_id_exist(research_id):
        try:
            result = Research.get_research_by_id(research_id=research_id)
            if result:
                return True
            return False
        except ObjectDoesNotExist:
            return False

    @staticmethod
    def get_research_by_id(research_id):
        result = Research.objects.filter(id=research_id).first()
        return result


class ResearchAttending(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.SET_NULL, null=True)
    research = models.ForeignKey(Research, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
