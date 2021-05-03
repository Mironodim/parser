from django.db import models

from django.db import models

class Job(models.Model):
    my_day = models.CharField(blank=True,max_length=50, verbose_name='ДН')
    my_time = models.CharField(blank=True,max_length=50, verbose_name='Дата')
    strana = models.CharField(blank=True,max_length=50, verbose_name='Страна')
    championat = models.CharField(blank=True,max_length=50, verbose_name='Чампионат')
    score_1 = models.CharField(blank=True,max_length=50,verbose_name='Счет')
    score_2 = models.CharField(blank=True,max_length=50,verbose_name='Счет')
    score1t_1 = models.CharField(blank=True, max_length=50,verbose_name='Счет1Т')
    score1t_2 = models.CharField(blank=True, max_length=50,verbose_name='Счет1Т')
    items1 = models.CharField(blank=True, max_length=50, verbose_name='Команда 1')
    items2 = models.CharField(blank=True, max_length=50, verbose_name='Команда 2')
    p1 = models.CharField(blank=True,max_length=50, verbose_name='П1')
    x = models.CharField(blank=True,max_length=50, verbose_name='Х')
    p2 = models.CharField(blank=True,max_length=50, verbose_name='П2')
    f1_0 = models.CharField(blank=True,max_length=50, verbose_name='Ф1(0)')
    f2_0 = models.CharField(blank=True,max_length=50, verbose_name='Ф2(0)')
    p1x = models.CharField(blank=True,max_length=50, verbose_name='П1Х')
    xp2 = models.CharField(blank=True,max_length=50, verbose_name='ХП2')
    tm = models.CharField(blank=True,max_length=50, verbose_name='ТМ')
    tb = models.CharField(blank=True,max_length=50, verbose_name='ТБ')
    oz = models.CharField(blank=True,max_length=50, verbose_name='ОЗ-ДА')
    p1_p1 = models.CharField(blank=True,max_length=50, verbose_name='П1/П1')
    x_p1 = models.CharField(blank=True,max_length=50, verbose_name='Н/П1')
    p2_p1 = models.CharField(blank=True,max_length=50, verbose_name='П2/П1')
    p1_x = models.CharField(blank=True,max_length=50, verbose_name='П1/Н')
    x_x = models.CharField(blank=True,max_length=50, verbose_name='Н/Н')
    p2_x = models.CharField(blank=True,max_length=50, verbose_name='П2/Н')
    p1_p2 = models.CharField(blank=True,max_length=50, verbose_name='П1/П2')
    x_p2 = models.CharField(blank=True, max_length=50, verbose_name='Н/П2')
    p2_p2 = models.CharField(blank=True,max_length=50, verbose_name='П2/П2')

    def __str__(self):
        return f'{self.my_day}, {self.my_time}, {self.strana}, {self.championat}, {self.items1}, {self.items2}'

    class Meta:
        verbose_name = 'Игры'
        verbose_name_plural = 'Игры'
        ordering = ['my_time']# фильтр по времени и дате
