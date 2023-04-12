from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON

from app.extensions.db_config import Base


class OpenedEmail(Base):
    """A table to store all read email events

    Attributes:
        mandrill_id (str): The mandrill id from mailchimp
        mandrill_ip (str): The mandrill ip from mailchimp
        mandrill_ts (int): The timestamp when the event happened on Mandrill platform
        location (dict): The place where the email was read
        user_agent (dict): The way the email was read
    """

    def __init__(
        self,
        mandrill_id=None,
        mandrill_ip=None,
        mandrill_ts=None,
        location=None,
        user_agent=None,
        subject=None,
        recipient_email=None,
        sender_email=None,
    ):
        self.mandrill_id = mandrill_id
        self.mandrill_ip = mandrill_ip
        self.mandrill_ts = mandrill_ts
        self.location = location
        self.user_agent = user_agent
        self.subject = subject
        self.recipient_email = recipient_email
        self.sender_email = sender_email

    __tablename__ = "opened_email"

    mandrill_id = Column(String)
    mandrill_ip = Column(String)
    mandrill_ts = Column(Integer)
    location = Column(JSON)
    user_agent = Column(JSON)
    subject = Column(String)
    recipient_email = Column(String)
    sender_email = Column(String)
