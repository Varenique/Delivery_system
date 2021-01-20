import pytest


@pytest.mark.parametrize("body, description", [({"name": 5}, "Required data not correct, doesn\'t match format"),
                                               ({"nami": "Hotfix"}, "Required data not correct, doesn\'t match format"),
                                               (None, "Required data not available(No data)")])
def test_put_wrong_format(test_client, get_mocker, body, description):
    response = test_client.put('/api/restaurants/0', json=body)
    assert response.status_code == 400
    assert {"description": "{}".format(description),
            "name": "Bad request"} == response.get_json()


@pytest.mark.parametrize("body, description", [
    ({"address": "Minsk", "id": 5, "work_time": "Monday-Sunday: 08:00 - 23:45", "phone_number": "+375297777777"},
     "Sent data not correct, doesn\'t match format"),
    ({"address": "Minsk", "id": "a", "work_time": "Monday-Sunday: 08:00 - 23:45", "phone_number": "+375297777777",
      "name": "Vasilki"},
     "Type of sent data not correct"),
    (None, "Required data not available(No data)")])
def test_post_wrong_format(test_client, get_mocker, body, description):
    response = test_client.post('/api/restaurants', json=body)
    assert response.status_code == 400
    assert {"description": "{}".format(description), "name": "Bad request"} == response.get_json()
