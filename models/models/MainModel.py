from django.db import models, connection

from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()

p_number_valid = RegexValidator(r'^[0-9]*$', 'Разрешены Только цифры')


class MainProject(models.Model):

    project_number = models.CharField('Номер Проекта', max_length=13, unique=True,
                                      validators=[p_number_valid],
                                      error_messages={'unique': 'Проект с таким номером уже существует'})

    project_name = models.CharField('Название проекта', max_length=255, blank=True, null=True)

    project_comment = models.TextField(verbose_name='Комментарий к проекту', blank=True, null=True, )

    project_created_by = models.ForeignKey(User, models.RESTRICT, 'projects_crd',
                                           verbose_name='Менеджер', )  # editable=False)

    project_created_date = models.DateTimeField('Дата создания проекта', auto_created=True, auto_now_add=True)

    project_updated_date = models.DateTimeField('Дата обновления проекта', auto_created=True, auto_now=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ('-project_created_date',)

    def __str__(self):
        return f'{self.project_name}'
