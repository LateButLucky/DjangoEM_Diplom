from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Module(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='название модуля')  # Увеличил длину до 100 символов для гибкости
    description = models.TextField(verbose_name='описание модуля')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'модуль'
        verbose_name_plural = 'модули'


class Lesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name='модуль')
    name = models.CharField(max_length=100,
                            verbose_name='название урока')  # Увеличил длину до 100 символов для гибкости
    description = models.TextField(verbose_name='описание урока')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
