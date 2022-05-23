from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.conf import settings

from .utils import slugify_instance_title

User = settings.AUTH_USER_MODEL

# Create your models here.
class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups) 

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

    def public(self):
        now = timezone.now()
        return self.get_queryset().filter(make_public=True, published_at__lte=now)

class Article(models.Model):
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#model-field-types
    # Django model-field-types
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    make_public = models.BooleanField(default=False, null=True, blank=True)
    published_at = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    tags = models.TextField(blank=True, null=True, help_text='Use commas to separate tags')
    
    objects=ArticleManager()

    @property
    def name(self):
        return self.title
    
    # def get_absolute_url(self):
    #     # return f'/articles/{self.slug}/'
    #     return reverse("articles:detail", kwargs={"slug": self.slug})

    def get_absolute_url(self):
        return f"/api/articles/{self.pk}/"

    @property
    def endpoint(self):
        return self.get_absolute_url()

    @property
    def path(self):
        return f"/articles/{self.pk}/"

    def is_public(self):
        if self.published_at is None:
            return False
        if self.make_public is None:
            return False
        now = timezone.now()
        is_in_past = now >= self.published_at
        return is_in_past and self.make_public

    def get_tags_list(self):
        if not self.tags:
            return []
        return [x.lower().strip() for x in self.tags.split(',')]

    def save(self, *args, **kwargs):
        if self.tags:
            if self.tags.endswith(","):
                self.tags = self.tags[:-1]
            if self.tags.startswith(","):
                self.tags = self.tags[1:]
            self.tags = f"{self.tags}".lower()
        if self.make_public and self.published_at is None:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)
