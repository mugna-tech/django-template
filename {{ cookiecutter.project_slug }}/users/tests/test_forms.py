import pytest

from django.test import override_settings

from users.forms import AllAuthPasswordResetForm


@pytest.mark.django_db
class TestAllAuthPasswordResetForm:
    @pytest.fixture(autouse=True)
    def setup(request):
        request.scheme = "http"
        yield

    @override_settings(ACCOUNT_AUTHENTICATION_METHOD="email")
    def test_save_using_email(request, user, mailoutbox):
        form = AllAuthPasswordResetForm(data={"email": user.email})

        assert form.is_valid()

        email = form.save(request=request)

        # checks if email sent
        assert len(mailoutbox) == 1
        assert mailoutbox[0].to == [user.email]

        assert email == user.email

    @override_settings(ACCOUNT_AUTHENTICATION_METHOD="username")
    def test_using_username(request, user, mailoutbox):
        form = AllAuthPasswordResetForm(data={"email": user.email})

        assert form.is_valid()

        email = form.save(request=request)

        # checks if email sent
        assert len(mailoutbox) == 1
        assert mailoutbox[0].to == [user.email]

        assert email == user.email
