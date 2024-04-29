from django.db import models
from django.utils import timezone
from utils.slugify import slugify_field


class ActiveModelManager(models.Manager):
    def get_queryset(self):
        return super(ActiveModelManager, self).get_queryset().filter(is_active=True)


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_active = models.BooleanField(default=True, verbose_name='Активный?')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    objects = models.Manager()
    active_objects = ActiveModelManager()

    class Meta:
        abstract = True

    def delete(self, hard=False, **kwargs):
        if hard:
            super(BaseModel, self).delete()
        else:
            self.is_active = False
            self.save()


class SlugModel(BaseModel):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name='Название')
    slug = models.CharField(max_length=255,
                            unique=True,
                            blank=True, null=True,
                            editable=False,
                            verbose_name='Название в ссылке', )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify_field(self.name, self)
        return super(SlugModel, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )

    class Meta:
        abstract = True
