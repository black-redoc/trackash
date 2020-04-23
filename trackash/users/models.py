from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f"user_{instance.id}/{filename}"


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    image_profile = ImageField(
        _("Image Profile"), blank=True, null=True, upload_to=user_directory_path
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
