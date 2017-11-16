from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey('auth.User')
    GENDER_CHOICES = (
        ('ACRE','AC'),
        ('ALAGOAS','AL'),
        ('AMAPÁ','AP'),
        ('AMAZONAS','AM'),
        ('BAHIA','BA'),
        ('CEARÁ','CE'),
        ('DISTRITO FEDERAL','DF'),
        ('ESPÍRITO SANTO','ES'),
        ('GOIÁS','GO'),
        ('MARANHÃO', 'MA'),
        ('MATO GROSSO', 'MT'),
        ('MATO GROSSO DO SUL', 'MS'),
        ('MINAS GERAIS', 'MG'),
        ('PARÁ', 'PA'),
        ('PARAÍBA','PB'),
        ('PARANÁ','PR'),
        ('PERNAMBUCO','PE'),
        ('PIAUÍ','PI'),
        ('RIO DE JANEIRO', 'RJ'),
        ('RIO GRANDE DO NORTE','RN'),
        ('RIO GRANDE DO SUL', 'RS'),
        ('RONDÔNIA','RO'),
        ('RORAIMA', 'RR'),
        ('SANTA CATARINA','SC'),
        ('SÃO PAULO','SP' ),
        ('SERGIPE','SE'),
        ('TOCANTINS','TO'),

    )
    estado = models.CharField(max_length=100 , choices=GENDER_CHOICES, 
        blank=True, null=True)
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    # def __str__(self):
    #     return self.estado


