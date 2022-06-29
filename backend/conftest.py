import pytest
from research.models import Research, ResearchField
from researcher.models import Researcher


@pytest.fixture
def research_data():
    pytest.research_filed_name = 'test field'
    pytest.research_name = 'test research'
    pytest.research_capacity = 25


@pytest.fixture
def research_field(research_data):
    field = ResearchField.create(name=pytest.research_filed_name)
    pytest.research_filed_id = field.id
    return field


@pytest.fixture
def research_fixture(research_data):
    return Research.create(name=pytest.research_name, field_id=pytest.research_filed_id,
                           capacity=pytest.research_capacity)


@pytest.fixture
def researcher_data():
    pytest.researcher_email = 'fixture@gmail.com'
    pytest.researcher_username = 'testUsername'
    pytest.researcher_password = 'testPassword'
    pytest.researcher_first_name = 'test_first_name'
    pytest.researcher_last_name = 'test_last_name'
    pytest.researcher_phone_number = 1234567890


@pytest.fixture
def researcher_fixture(researcher_data):
    return Researcher.create(email=pytest.researcher_email, username=pytest.researcher_username,
                             password=pytest.researcher_password, first_name=pytest.researcher_first_name,
                             last_name=pytest.researcher_last_name, phone_number=pytest.researcher_phone_number)
