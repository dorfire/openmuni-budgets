from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from uuidfield import UUIDField


class UserProfile(models.Model):
    """Extends Django's User with our project specific user fields"""

    user = models.OneToOneField(
        User
    )
    uuid = UUIDField(
        auto=True
    )

    class Meta:
        ordering = ['user']
        verbose_name = _('User profile')
        verbose_name_plural = _('User profiles')

    @models.permalink
    def get_absolute_url(self):
        return ('user_profile_detail', [self.uuid])

    def __unicode__(self):
        return self.user.username
