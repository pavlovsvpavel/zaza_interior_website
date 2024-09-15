from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

MAX_IMAGE_SIZE = 9 * 1024 * 1024

def validate_image_size(image):
    if image.size > MAX_IMAGE_SIZE:
        raise ValidationError(_('The maximum file size should not exceed 9MB'))

def validate_image_file_type(image):
    if image and not image.name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        raise ValidationError(_('Unsupported file type. Please upload an image file (.jpg, .jpeg, .png, .gif)'))