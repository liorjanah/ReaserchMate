from django.core.exceptions import ValidationError


class ValidateResearchField:
    def __init__(self, name):
        self.name = name

    def start_validation(self):
        from .models import ResearchField
        if ResearchField.is_name_exist(name=self.name):
            raise ValidationError("Invalid research field nane - research field already exist.")


class ValidateResearch:
    def __init__(self, name):
        self.name = name

    def start_validation(self):
        self.validate_research_name_unique()

    def validate_research_name_unique(self):
        from .models import Research
        if Research.is_research_name_exist(name=self.name):
            raise ValidationError("Invalid research nane - research already exist.")
