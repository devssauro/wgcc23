import json

from flask import Blueprint, request

from app.handlers import OpenedEmailHandler
from app.models import OpenedEmail

bp = Blueprint("mandrill", __name__, url_prefix="mandrill")


@bp.route("", methods=["HEAD"])
def mandrill_head():
    """Function to madrill test the webhook"""
    return "", 200


@bp.post("")
def mandrill_post():
    """Webhook for mandrill response"""
    mandrill_events = json.loads(request.form["mandrill_events"])
    ids = [mail["_id"] for mail in mandrill_events]
    found_ids = OpenedEmailHandler.find_emails_by_mandrill_id(
        ids=ids,
        return_only_mandrill_ids=True,
    )

    new_mails = [mail for mail in mandrill_events if mail["_id"] not in found_ids]
    mails_to_insert = []

    for mail in new_mails:
        mails_to_insert.append(
            OpenedEmail(
                mandrill_id=mail["_id"],
                mandrill_ip=mail["ip"],
                mandrill_ts=mail["ts"],
                location=mail["location"],
                user_agent=mail["user_agent_parsed"],
                subject=mail["msg"]["subject"],
                recipient_email=mail["msg"]["email"],
                sender_email=mail["msg"]["sender"],
            )
        )

    OpenedEmailHandler.bulk_upsert_email(mails_to_insert)

    return {"ids": found_ids}, 200
