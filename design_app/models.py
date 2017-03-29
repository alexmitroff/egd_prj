# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.flatpages.models import FlatPage as FlatPageOld

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
            help_text=_('Title image'), blank=True, null=True)
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
        return  self.name_ru

class Rubric(models.Model):
    """
    It defines rubric within degree
    """
    degree = models.ForeignKey(Degree, default=0)
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
    pic = models.ImageField('image',upload_to='degree/rubrics/',
            help_text=_('Title image'), blank=True, null=True)
    # --- alter save method to avoid useless images on HDD
    def save(self, *args, **kwargs):
        try:
            this = Rubric.objects.get(id=self.id)
            if this.pic != self.pic:
                this.pic.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = _("Degree rubric")
        verbose_name_plural = _("Degree rubrics")
        ordering = ['pos']
    def __str__(self):
        return "{0} | {1}".format(self.degree.name_ru, self.name_ru)

def programm_image_location(instance, filename):
    filename = filename.replace(" ","")
    if len(filename) > 100:
        filename = filename[:99]
    return 'programmes/{0}/{1}'.format(instance.slug, filename)
    
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
    rubric = models.ForeignKey(Rubric, blank=True, null=True)
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
    pic = models.ImageField(_('image'),upload_to=programm_image_location,
            help_text='Title image', blank=True, null=True)

    # --- alter save method to avoid useless images on HDD
    def save(self, *args, **kwargs):
        try:
            this = Programm.objects.get(id=self.id)
            if this.pic != self.pic:
                this.pic.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Programm")
        verbose_name_plural = _("Programmes")
        ordering = ['pos']
    def __str__(self):
        return self.name_ru

def programmimage_image_location(instance, filename):
    filename = filename.replace(" ","")
    if len(filename) > 100:
        filename = filename[:99]
    return 'programmes/{0}/images/{1}'.format(instance.programm.slug, filename)

class ProgrammImage(models.Model):
    pos = models.IntegerField(_('Position'),default=0)
    show = models.BooleanField(_('Show'), default=True)
    programm = models.ForeignKey(Programm, default = 0)
    name_en = models.CharField( _("Name in english"), max_length = 140,
            help_text=_("Name in english"), blank=True, null=True)
    name_ru = models.CharField( _("Name in russian"), max_length = 140,
            help_text=_("Name in russian"), blank=True, null=True)
    pic = models.ImageField(_('image'),upload_to=programmimage_image_location,
            help_text='image', blank=True, null=True)
    # --- alter save method to avoid useless images on HDD
    def save(self, *args, **kwargs):
        try:
            this = ProgrammImage.objects.get(id=self.id)
            if this.pic != self.pic:
                this.pic.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Programm image")
        verbose_name_plural = _("Programm images")
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


def image_location(instance, filename):
    filename = filename.replace(" ","")
    if len(filename) > 100:
        filename = filename[:99]
    return 'flatimages/{0}'.format(filename)

class FlatImage(models.Model):
    pic = models.ImageField('image',upload_to=image_location,
            help_text='Title image', blank=True, null=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"),auto_now=True)
    # --- alter save method to avoid useless images on HDD
    def save(self, *args, **kwargs):
        try:
            this = FlatImage.objects.get(id=self.id)
            if this.pic != self.pic:
                this.pic.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Flat image")
        verbose_name_plural = _("Flat images")
        ordering = ['modified']
    def __str__(self):
        return self.pic.url


def document_location(instance, filename):
    filename = filename.replace(" ","")
    if len(filename) > 100:
        filename = filename[:99]
    return 'programmes/{0}/{1}'.format(instance.slug, filename)

class Document(models.Model):
    pos = models.IntegerField(_('Position'),default=0)
    show = models.BooleanField(_('Show'), default=True)
    tag = models.ManyToManyField(Tag,related_name='documents')
    ## --- en locale
    name_en = models.CharField( _("Name in english"), max_length = 140,
            help_text=_("Name in english"), blank=True, null=True)
    ## --- ru locale
    name_ru = models.CharField( _("Name in russian"), max_length = 140,
            help_text=_("Name in russian"), blank=True, null=True)
    doc = models.FileField('image',upload_to=document_location,
            help_text='Title image', blank=True, null=True)
    # --- alter save method to avoid useless images on HDD
    def save(self, *args, **kwargs):
        try:
            this = Document.objects.get(id=self.id)
            if this.doc != self.doc:
                this.doc.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")
        ordering = ['pos']
    def __str__(self):
        return self.name_ru

def lab_image_location(instance, filename):
    filename = filename.replace(" ","")
    if len(filename) > 100:
        filename = filename[:99]
    return 'lab/{0}/{1}'.format(instance.slug, filename)

class Lab(models.Model):
    pos = models.IntegerField(_('Position'),default=0)
    show = models.BooleanField(_('Show'), default=True)
    slug = models.CharField( _('URL'), max_length = 140,
            help_text=_("it will shows up in address area"), default='slug')
    name_en = models.CharField( _("Name in english"), max_length = 140,
            help_text=_("Name in english"), blank=True, null=True)
    content_en = models.TextField(_('Content in english'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    name_ru = models.CharField( _("Name in russian"), max_length = 140,
            help_text=_("Name in russian"), blank=True, null=True)
    content_ru = models.TextField(_('Content in russian'),blank=True,
            null=True, help_text=_("use HTML for better result"))
    cover = models.ImageField(_('image'),upload_to=lab_image_location,
            help_text='cover image', blank=True, null=True)
    def save(self, *args, **kwargs):
        try:
            this = Lab.objects.get(id=self.id)
            if this.cover != self.cover:
                this.cover.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = _("Lab")
        verbose_name_plural = _("Labs")
        ordering = ['pos']
    def __str__(self):
        return self.name_ru
