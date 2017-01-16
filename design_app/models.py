from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class NewsCategory(models.Model):
    """
    News category used for group news.
    News category also defines news color theme.

    """
    name_en = models.CharField( _("Name in english"), max_length = 50,
            help_text=_("Name in english"))
    name_ru = models.CharField( _("Name in russian"), max_length = 50,
            help_text=_("Name in russian"))
    color = models.CharField( _("Category  color"), max_length = 50,
            help_text=_("HEX number with # like #8f5642"), default="#CCCCCC")
    class Meta:
        verbose_name = _("News category")
        verbose_name_plural = _("News categories")		
    def __str__(self):
        return self.name_ru

class NewsItem(models.Model):
    category = models.ForeignKey(NewsCategory, default = 0)	
    title_en = models.CharField( _("Title in english"), max_length = 50,
            help_text=_("Title in english"), blank=True, null=True)
    content_en = models.TextField(_('Content in english'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    title_ru = models.CharField( _("Title in russian"), max_length = 50,
            help_text=_("Title in russian"), blank=True, null=True)
    content_ru = models.TextField(_('Content in russian'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"),auto_now=True)
    publish = models.BooleanField(_("Published"), default = True) 
    class Meta:
        verbose_name = _("News item")
        verbose_name_plural = _("News items")
        ordering = ["created"]
    def __str__(self):
        return self.title_ru



