import pytest
from .models import Research
from django.core.exceptions import ValidationError


@pytest.mark.django_db
class TestResearchModel:
    def test_unique_research_name(self, research_fixture, research_data):
        with pytest.raises(ValidationError, match='Invalid research nane - research already exist.'):
            Research.create(name=pytest.research_name, field_id=pytest.research_filed_id,
                            capacity=pytest.research_capacity)

    def test_is_name_exist(self, research_fixture):
        assert Research.is_research_name_exist(research_fixture.name)
        assert not Research.is_research_name_exist('this name should not exist')
