from dj_rest_auth.serializers import PasswordResetSerializer

from users.forms import AllAuthPasswordResetForm


class PasswordResetSerializer(PasswordResetSerializer):
    password_reset_form_class = AllAuthPasswordResetForm
