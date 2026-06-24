import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile

# Get the user model
User = get_user_model()

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a Profile instance when a new User is created.
    """
    if created:
        Profile.objects.create(user=instance)
        logger.info(f"Profile created for user: {instance.get_full_name}")
        # Send a welcome email to the user (optional)


