from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    photo = models.ImageField(upload_to='imgs', null=True, verbose_name='Изображение')
    title_en = models.CharField(max_length=200, null=True, verbose_name='Название на английском')
    title_jp = models.CharField(max_length=200, null=True, verbose_name='Название на японском')
    description = models.TextField(null=True, verbose_name='Описание')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name='Родительский покемон')
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name_plural = 'Покемоны'    
        verbose_name = 'Покемоны'    

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Появился в')
    disappeared_at = models.DateTimeField(verbose_name='Исчез в')
    level = models.IntegerField(verbose_name='Уровень')
    health = models.IntegerField(verbose_name='Здоровье')
    strange = models.IntegerField(verbose_name='Странность')
    defence = models.IntegerField(verbose_name='Защита')
    stamina = models.IntegerField(verbose_name='Выносливость')
    
    def __str__(self):
        return f'{self.pokemon}: ({self.lat}, {self.lon})'
    
    class Meta:
        verbose_name_plural = 'Экземпляры покемонов'
        verbose_name = 'Экземпляры покемонов'