from django.db import models

# Create your models here.
class TibetToPinyin(models.Model):
    """Model definition for TibetToPinyin."""
    tibet = models.CharField(max_length=10)
    pinyin = models.CharField(max_length=10, blank=True, null=True)


    class Meta:
        """Meta definition for TibetToPinyin."""

        verbose_name = 'Tibet To Pinyin'
        verbose_name_plural = 'Tibet To Pinyin'

    def __str__(self):
        """Unicode representation of Tibet To Pinyin."""
        return self.tibet
