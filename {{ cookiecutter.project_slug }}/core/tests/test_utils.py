import pytest

from core.utils import get_upload_path, send_email


@pytest.mark.django_db
def test_send_email(request, mailoutbox):
    request.scheme = "http"

    send_email(
        request,
        "subject",
        "account/email/password_reset_key_message.txt",
        ["to@example.com"],
    )

    assert len(mailoutbox) == 1
    assert mailoutbox[0].subject == "subject"
    assert mailoutbox[0].to == ["to@example.com"]


@pytest.mark.django_db
def test_get_upload_path(user):
    assert get_upload_path(user, "test.txt") == "user/test.txt"
