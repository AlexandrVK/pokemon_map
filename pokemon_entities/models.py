from django.db import models

class Pokemon(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название"
    )
    title_en = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Название на английском"
    )
    title_jp = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Название на японском"
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
    )
    photo = models.ImageField(
        upload_to="imgs",
        null=True,
        verbose_name="Изображение"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Из кого развился покемон",
        related_name="evolved_from"
    )

    class Meta:
        verbose_name = "Покемон"
        verbose_name_plural = "Покемоны"

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name="Покемон",
        related_name="entities"
    )
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Появился в")
    disappeared_at = models.DateTimeField(verbose_name="Исчез в")
    level = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Уровень"
    )
    health = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Здоровье"
    )
    strange = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Странность"
    )
    defence = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Защита"
    )
    stamina = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Выносливость"
    )

    class Meta:
        verbose_name = "Экземпляр покемона"
        verbose_name_plural = "Экземпляры покемонов"

    def __str__(self):
        return f"{self.pokemon}: ({self.lat}, {self.lon})"
