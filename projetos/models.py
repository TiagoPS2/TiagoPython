from django.db import models

# Create your models here.
class Projeto(models.Model):
    titulo = models.CharField(
        verbose_name = "projetos",
        max_length=100,
        help_text="porjetos",
    )
    descricao = models.TextField(
        verbose_name = "descricao do projeto", help_text="descricao do projeto"    
    )

    tecnologia = models.CharField(
        max_length=20,
        verbose_name = "django",
        help_text="django",
    )
    imagem = models.FileField(
        verbose_name="Imagem do projeto",
        help_text="Imagem do projeto",
        upload_to="imagens/",
        blank=True,
    )

    class Meta:
        db_table: str = 'projeto'
        verbose_name: str = 'projeto'
        verbose_name_plural: str = 'projetos'
