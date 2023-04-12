from app.extensions.db_config import db
from app.models import OpenedEmail


class OpenedEmailHandler:
    """Class to handle all the operations related to opened_emails table"""

    @staticmethod
    def upsert_email(email: OpenedEmail) -> OpenedEmail:
        """Insert a new email or update a existing one"""
        db.session.add(email)
        db.session.commit()
        return email

    @staticmethod
    def bulk_upsert_email(emails: list[OpenedEmail]) -> list[OpenedEmail]:
        """Insert new emails or update existing ones"""
        for email in emails:
            db.session.add(email)
        db.session.commit()
        return emails

    @staticmethod
    def find_emails_by_mandrill_id(
        ids: list[str], return_only_mandrill_ids: bool = False
    ) -> list[OpenedEmail] | list[str]:
        """Query all emails by mandrill id's from webhook

        Args:
            ids (list[str]): list of mandrill ids'
            return_only_mandrill_ids (bool): to return only the id values
        """

        if return_only_mandrill_ids:
            query = OpenedEmail.query.with_entities(
                OpenedEmail.mandrill_id,
            ).filter(OpenedEmail.active, OpenedEmail.mandrill_id.in_(ids))
            return [email.mandrill_id for email in query]

        query = OpenedEmail.query.filter(OpenedEmail.active, OpenedEmail.mandrill_id.in_(ids))

        return [email for email in query]
