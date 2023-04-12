import json
from unittest.mock import patch

from flask import Flask

from app.models import OpenedEmail


class TestMandrillHead:
    """Test the HEAD request to Mandrill webhook"""

    @staticmethod
    def test_success(sample_app: Flask) -> None:
        response = sample_app.head("/webhook/mandrill")
        assert response.status_code == 200
        assert response.data == b""


class TestMandrillPost:
    """Test the POST request to Mandrill webhook"""

    @staticmethod
    def test_success(
        sample_app: Flask, sample_request_1: list[dict], sample_opened_email_1: OpenedEmail
    ) -> None:
        """Test if the API triggers the HEAD function to validate mandrill webhook
        Args:
            sample_app(App): The Flask application
        """
        with (
            patch(
                "app.handlers.opened_email_handler.OpenedEmailHandler.find_emails_by_mandrill_id"
            ) as find_emails_by_mandrill_id,
            patch(
                "app.handlers.opened_email_handler.OpenedEmailHandler.bulk_upsert_email"
            ) as bulk_upsert_email,
        ):
            find_emails_by_mandrill_id.return_value = [sample_request_1[1]["_id"]]
            bulk_upsert_email.return_value = [sample_opened_email_1]
            response = sample_app.post(
                "/webhook/mandrill", data={"mandrill_events": json.dumps(sample_request_1)}
            )
            assert response.status_code == 200
            assert response.json == {"ids": [sample_request_1[1]["_id"]]}
