from django.db import models



class Projects(models.Model):
    project = models.CharField(
        verbose_name='Тип задачи', 
        max_length=100,
        null=False
    )
    description = models.TextField(
        max_length=3000, 
        blank=True, 
        null=True, 
        default=' ', 
        verbose_name='Полное описание'
    )
    created_at = models.DateField(
        verbose_name='Дата начала',
        null=False
    )
    deadline = models.DateField(
        verbose_name='Дата окончания',
        blank=True, 
        null=True 
    )

    def __str__(self) -> str:
        return f'{self.project}'