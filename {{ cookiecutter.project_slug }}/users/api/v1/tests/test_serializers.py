from users.api.v1.serializers import PasswordResetSerializer
from users.forms import AllAuthPasswordResetForm


class TestPasswordResetSerializer:
    def test_password_reset_form_class(self):
        serializer = PasswordResetSerializer()
        assert serializer.password_reset_form_class == AllAuthPasswordResetForm
