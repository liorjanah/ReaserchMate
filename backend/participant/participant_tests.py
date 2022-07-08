import pytest
from .models import Participant
from django.core.exceptions import ValidationError


@pytest.mark.django_db
class TestParticipantModel:
    def test_email_validation(self, participant_fixture, participant_data):
        with pytest.raises(ValidationError, match='Enter a valid email address.'):
            Participant.create(email='no email', username='test_name_validation_username',
                               password=pytest.participant_password, first_name=pytest.participant_first_name,
                               last_name=pytest.participant_last_name, phone_number=pytest.participant_phone_number)

    def test_email_unique(self, participant_fixture, participant_data):
        with pytest.raises(ValidationError, match='Invalid email - email already exist.'):
            Participant.create(email=pytest.participant_email, username='test_name_validation_username',
                               password=pytest.participant_password, first_name=pytest.participant_first_name,
                               last_name=pytest.participant_last_name, phone_number=pytest.participant_phone_number)

    def test_name_validation(self, participant_fixture, participant_data):
        with pytest.raises(ValidationError, match='Invalid username - username already exist.'):
            Participant.create(email='test_name_validation@gmail.com', username=pytest.participant_username,
                               password=pytest.participant_password, first_name=pytest.participant_first_name,
                               last_name=pytest.participant_last_name, phone_number=pytest.participant_phone_number)

    def test_phone_validation_len(self, participant_fixture, participant_data):
        with pytest.raises(ValidationError, match='Invalid phone - phone should be 10 digits.'):
            Participant.create(email='test_name_validation@gmail.com', username='test_name_validation_username',
                               password=pytest.participant_password, first_name=pytest.participant_first_name,
                               last_name=pytest.participant_last_name, phone_number=123)

    def test_phone_validation_str(self, participant_fixture, participant_data):
        with pytest.raises(ValidationError, match='Invalid phone - phone should be number.'):
            Participant.create(email='test_name_validation@gmail.com', username='test_name_validation_username',
                               password=pytest.participant_password, first_name=pytest.participant_first_name,
                               last_name=pytest.participant_last_name, phone_number='123')
