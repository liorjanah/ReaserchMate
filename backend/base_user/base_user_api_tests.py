import pytest


def send_request(client, url, type='get', data=None, content_type='application/json'):
    if data is None:
        data = {}
    if type == 'get':
        return client.get(url)
    if type == 'post':
        return client.post(url, data=data, content_type=content_type)


@pytest.mark.django_db
class TestBaseUserAPI:
    def test_login_api_valid(self, client, participant_fixture, participant_data):
        data = {
            'username': pytest.participant_username,
            'password': pytest.participant_password
        }

        response = send_request(client, '/api/auth/login', 'post', data)
        assert response.status_code == 200
        assert response.data['user']['user']['id'] == participant_fixture.base_user.user.id
        assert response.data['user']['user']['username'] == participant_fixture.base_user.user.username
        assert response.data['user']['user']['email'] == participant_fixture.base_user.user.email
        assert response.data['user']['user']['first_name'] == participant_fixture.base_user.user.first_name
        assert response.data['user']['user']['last_name'] == participant_fixture.base_user.user.last_name
        assert response.data['user']['id'] == participant_fixture.base_user.id
        assert response.data['user']['phone_number'] == participant_fixture.base_user.phone_number
        assert 'token' in response.data.keys()

    def test_login_api_invalid(self, client):
        data = {
            'username': 'invalid',
            'password': 'invalid'
        }

        response = send_request(client, '/api/auth/login', 'post', data)
        assert response.status_code == 400
        assert 'Incorrect Credentials' in response.data['non_field_errors'][0]
