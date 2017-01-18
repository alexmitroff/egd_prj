# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class NewsCategory(models.Model):
    """
    News category used for group news.
    News category also defines news color theme.
    """
    ## --- en locale
    name_en = models.CharField( _("Name in english"), max_length = 50,
            help_text=_("Name in english"))
    ## --- ru locale
    name_ru = models.CharField( _("Name in russian"), max_length = 50,
            help_text=_("Name in russian"))
    color = models.CharField( _("Category  color"), max_length = 7,
            help_text=_("HEX number with # like #8f5642"), default="#CCCCCC")
    class Meta:
        verbose_name = _("News category")
        verbose_name_plural = _("News categories")		
    def __str__(self):
        return self.name_ru

class NewsItem(models.Model):
    category = models.ForeignKey(NewsCategory, default = 0)	
    ## --- en locale
    title_en = models.CharField( _("Title in english"), max_length = 140,
            help_text=_("Title in english"), blank=True, null=True)
    content_en = models.TextField(_('Content in english'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    ## --- ru locale
    title_ru = models.CharField( _("Title in russian"), max_length = 140,
            help_text=_("Title in russian"), blank=True, null=True)
    content_ru = models.TextField(_('Content in russian'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    ## --- additional
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"),auto_now=True)
    publish = models.BooleanField(_("Published"), default = True) 
    class Meta:
        verbose_name = _("News item")
        verbose_name_plural = _("News items")
        ordering = ["created"]
    def __str__(self):
        return self.title_ru

class Degree(models.Model):
    """
    It defines degree
    """
    pos = models.IntegerField(_('Position'),default=0)
    show = models.BooleanField(_('Show'), default=True)
    slug = models.CharField( _('URL'), max_length = 140,
            help_text=_("it will shows up in address area"), default='slug')
    ## --- en locale
    name_en = models.CharField( _("Name in english"), max_length = 140,
            help_text=_("Name in english"), blank=True, null=True)
    content_en = models.TextField(_('Content in english'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    ## --- ru locale
    name_ru = models.CharField( _("Name in russian"), max_length = 140,
            help_text=_("Name in russian"), blank=True, null=True)
    content_ru = models.TextField(_('Content in russian'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    pic = models.ImageField('image',upload_to='degree/titles/',
            help_text='Title image', blank=True, null=True)
    # --- alter save method to avoid useless images on HDD
    def save(self, *args, **kwargs):
        try:
            this = Degree.objects.get(id=self.id)
            if this.pic != self.pic:
                this.pic.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = _("Degree")
        verbose_name_plural = _("Degrees")
        ordering = ['pos']
    def __str__(self):
        return self.name_ru

class Programm(models.Model):
    """
    all about programm
    """
    INTRAMURAL = 0
    EXTRAMURAL = 1
    EVENING = 2
    FORM_CHOICES = (            
        (INTRAMURAL,_('intramural')),
        (EXTRAMURAL,_('extramural')),
        (EVENING,_('evening classes')),
            )
    pos = models.IntegerField(_('Position'),default=0)
    show = models.BooleanField(_('Show'), default=True)
    degree = models.ForeignKey(Degree, default = 0)
    form = models.IntegerField(_('Form'),choices=FORM_CHOICES, default=INTRAMURAL)
    duration = models.IntegerField(_('Duration'), default=4,
            help_text=_("in years"))
    color = models.CharField( _("Programm  color"), max_length = 7,
            help_text=_("HEX number with # like #8f5642"), default="#CCCCCC")
    slug = models.CharField( _('URL'), max_length = 140,
            help_text=_("it will shows up in address area"), default='slug')
    ## --- en locale
    name_en = models.CharField( _("Name in english"), max_length = 140,
            help_text=_("Name in english"), blank=True, null=True)
    short_en = models.TextField(_('Short in english'),blank=True,
            null=True, help_text=_("140 symbols"))
    content_en = models.TextField(_('Content in english'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    summary_en = models.TextField(_('Summary in english'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    courses_en = models.TextField(_('Courses in english'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    inter_en = models.TextField(_('International in english'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    tech_en = models.TextField(_('Tech in english'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    ## --- ru locale
    name_ru = models.CharField( _("Name in russian"), max_length = 140,
            help_text=_("Name in russian"), blank=True, null=True)
    short_ru = models.TextField(_('Short in russian'),blank=True,
            null=True, help_text=_("140 symbols"))
    content_ru = models.TextField(_('Content in russian'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    summary_ru = models.TextField(_('Summary in russian'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    courses_ru = models.TextField(_('Courses in russian'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    inter_ru = models.TextField(_('International in russian'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    tech_ru = models.TextField(_('Tech in russian'),blank=True,
            null=True, help_text=_("use HTML for better result"))

    class Meta:
        verbose_name = _("Programm")
        verbose_name_plural = _("Programmes")
        ordering = ['pos']
    def __str__(self):
        return self.name_ru

class Tag(models.Model):
    word = models.CharField(_("Word"), max_length=35)
    
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
    def __str__(self):
        return self.word

class Unit(models.Model):
    """
    Some additional info like exams or so..
    """
    pos = models.IntegerField(_('Position'),default=0)
    show = models.BooleanField(_('Show'), default=True)
    tag = models.ManyToManyField(Tag,related_name='units')
    ## --- en locale
    name_en = models.CharField( _("Name in english"), max_length = 140,
            help_text=_("Name in english"), blank=True, null=True)
    content_en = models.TextField(_('Content in english'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    ## --- ru locale
    name_ru = models.CharField( _("Name in russian"), max_length = 140,
            help_text=_("Name in russian"), blank=True, null=True)
    content_ru = models.TextField(_('Content in russian'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Units")
        ordering = ['pos']
    def __str__(self):
        return self.name_ru

