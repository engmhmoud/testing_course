import json
import logging

import pytest
from company.models import Company
from django.urls import reverse
from rest_framework import status

logger_name = "CORONA_LOG"
logging.getLogger(logger_name)

# @pytest.mark.django_db

companies_url = reverse("company:companies-list")
pytestmark = pytest.mark.django_db


def test_zero_companies_should_return_empty_list(client):

    response = client.get(companies_url)
    assert response.status_code == status.HTTP_200_OK
    assert json.loads(response.content) == []


def test_one_company_exist_should_return_success(client):
    item = Company.objects.create(name="Amazonn")

    response = client.get(companies_url)
    res_data = json.loads(response.content)[0]
    assert response.status_code == status.HTTP_200_OK
    assert res_data.get("name") == item.name
    assert res_data.get("status") == "Stable"

    # assert res_data.get("notest") == None or res_data.get("notest") == ""
    assert res_data.get("notest") is None


def test_create_company_without_parameters_should_failed(client):

    response = client.post(companies_url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert json.loads(response.content) == {"name": ["This field is required."]}


@pytest.mark.xfail
def test_create_company_with_name_only_should_create(client):

    response = client.post(companies_url, {"name": "Amazon"})
    res_data = json.loads(response.content)[0]
    assert response.status_code == status.HTTP_201_CREATED
    assert res_data.get("status") == "Stable"


def test_create_company_with_name_and_right_status_should_success(client):

    response = client.post(companies_url, {"name": "Amazon"})
    assert response.status_code == status.HTTP_201_CREATED


def test_create_company_with_name_and_wrong_status_should_failed(client):

    response = client.post(companies_url, {"name": "Amazon", "status": "google"})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    print(str(response.content))
    assert "is not a valid choice" in str(response.content)


def raise_covid_error():
    raise ValueError("Error Covid")


def test_will_loge_something():
    try:
        raise_covid_error()
    except ValueError as e:
        logging.warning(f"logging{str(e)}")


def test_testing(caplog):

    test_will_loge_something()
    assert "Covid" in caplog.text


def test_testing_info(caplog):
    with caplog.at_level(logging.INFO) as e:
        logging.info(f"info:{str(e)}")
    assert "Covid" in caplog.text
