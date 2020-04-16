from django.db import models


class Project(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Название проекта, должно быть уникальным",
        unique=True,
        verbose_name='Наименование'
    )
    customer = models.CharField(
        max_length=50,
        verbose_name='Заказчик'
    )
    area = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Площадь'
    )
    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Стоимость'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text="Заметки, чтобы не забыть",
        blank=True,
        default='',
    )

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return f"Проект {self.name} ({self.customer})"


class Job(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Наименование'
    )

    def __str__(self):
        return f"Работа {self.name}"

    description = models.TextField(
        verbose_name='Описание',
        help_text="Заметки, чтобы не забыть",
        blank=True,
        default='',
    )

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"


class Worker(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='ФИО'
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Цена'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text="Примечание",
        blank=True,
        default='',
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.PROTECT,
        related_name='workers',
        verbose_name='Работа',
        help_text="Работа, которую выполняет данный работник",
    )

    def __str__(self):
        return f"Работник {self.name}"

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"


class Incomes(models.Model):
    date = models.DateField(
        verbose_name='Дата'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        related_name='incomes',
        verbose_name='Проект',
    )
    sum = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Сумма'
    )

    def __str__(self):
        return f"Поступления {self.sum} от {self.date}"

    class Meta:
        verbose_name = "Поступления"
        verbose_name_plural = "Поступления"


class Outcomes(models.Model):
    date = models.DateField(
        verbose_name='Дата'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        related_name='outcomes',
        verbose_name='Проект',
    )
    Worker = models.ForeignKey(
        Worker,
        on_delete=models.PROTECT,
        related_name='payments',
        verbose_name='Работник',
    )
    sum = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Сумма'
    )

    def __str__(self):
        return f"Расходы на сумму {self.sum} от {self.date}"

    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"


class ProjectMembers(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        related_name='members',
        verbose_name='Проект',
    )
    worker = models.ForeignKey(
        Worker,
        on_delete=models.PROTECT,
        related_name='projects',
        verbose_name='Работник',
    )
    amount = models.DecimalField(max_digits=13, decimal_places=2, verbose_name='Объем')
    sum = models.DecimalField(max_digits=13, decimal_places=2, verbose_name='Сумма')

    def __str__(self):
        return f"Участник проекта на сумму {self.sum} от {self.amount}"

    class Meta:
        verbose_name = "Участник проекта"
        verbose_name_plural = "Участники проекта"
