import pytest
from .models import ResearchField
from django.core.exceptions import ValidationError


@pytest.mark.django_db
class TestResearchFieldModel():
    def test_unique_research_field_name(self, research_field, research_data):
        with pytest.raises(ValidationError, match='Invalid research field nane - research field already exist.'):
            ResearchField.create(name=pytest.research_filed_name)

    def test_get_by_id(self, research_field):
        field = ResearchField.get_field_id(research_field.id)
        assert field.id == research_field.id
        assert field.name == research_field.name

    def test_is_name_exist(self, research_field):
        assert ResearchField.is_name_exist(research_field.name)
        assert not ResearchField.is_name_exist('this name should not exist')
