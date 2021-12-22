import json
import logging

import pytest
from company.models import Company
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

logger_name = "CORONA_LOG"
logging.getLogger(logger_name)
# @pytest.mark.django_db


class TestCompany(TestCase):
    def setUp(self) -> None:

        self.client = Client()
        self.companies_url = reverse("company:companies-list")

        def tearDown(self) -> None:

            pass


class TestGetCompany(TestCompany):
    def test_zero_companies_should_return_empty_list(self):

        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [])

    def test_one_company_exist_should_return_success(self):
        item = Company.objects.create(name="Amazonn")

        response = self.client.get(self.companies_url)
        res_data = json.loads(response.content)[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res_data.get("name"), item.name)
        self.assertEqual(res_data.get("status"), "Stable")

        self.assertEqual(res_data.get("notest"), None)


class TestPostCompany(TestCompany):
    def test_create_company_without_parameters_should_failed(self):

        response = self.client.post(self.companies_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), {"name": ["This field is required."]})

    @pytest.mark.xfail
    def test_create_company_with_name_only_should_create(self):

        response = self.client.post(self.companies_url, {"name": "Amazon"})
        res_data = json.loads(response.content)[0]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res_data.get("status"), "Stable")

    def test_create_company_with_name_and_right_status_should_success(self):

        response = self.client.post(self.companies_url, {"name": "Amazon"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_company_with_name_and_wrong_status_should_failed(self):

        response = self.client.post(self.companies_url, {"name": "Amazon", "status": "google"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print(str(response.content))
        self.assertIn("is not a valid choice", str(response.content))


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
