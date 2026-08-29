from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, FileExtensionValidator
from django.core.exceptions import ValidationError

def validate_image_size(image):
    # Restrict uploads to a max of 5MB
    max_size_mb = 5
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Image size cannot exceed {max_size_mb}MB.")

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"  # Allows clean access via user.profile
    )
    img = models.ImageField(
        upload_to="profile_pictures/%Y/%m/",  # Organizes uploads by year/month
        blank=True,
        null=True,
        validators=[
            validate_image_size,
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])
        ],
        help_text="Upload a profile picture (JPEG, PNG, or WebP up to 5MB)."
    )
    bio = models.TextField(
        blank=True,
        default="",
        max_length=500,
        validators=[MaxLengthValidator(500)],
        help_text="Tell readers a bit about yourself (max 500 characters)."
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"