import os
from typing import Any

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(
    request: HttpRequest,
    subject: str,
    template: str,
    recipients: list[str],
    data: dict[str, Any] = {},
):
    """
    This function sends an email using a selected template.
    Arguments:
        subject: the subject of the email
        template: the template to be used for the email
        recipient: a list of recipients the email will be sent to
        data: a dictionary to be added as context variables in the email
    """
    context = {
        "current_site": Site.objects.get_current(),
        "protocol": request.scheme,
    }
    context.update(data)
    html_content = render_to_string(template, context)
    text_content = strip_tags(html_content)

    send_mail(
        subject=subject,
        message=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipients,
        fail_silently=False,
        html_message=html_content,
    )


def get_upload_path(instance: object, filename: str) -> str:
    return os.path.join(instance.__class__.__name__.lower(), filename)
