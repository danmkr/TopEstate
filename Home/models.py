from django.db import models


class Search(models.Model):

    optiuni_proprietati = (
        ('apartamente', 'Apartamente'),
        ('case/vile', 'Case/Vile'),
        ('terenuri', 'Terenuri')
    )

    optiuni_achizitie = (
        ('de vanzare', 'De vanzare'),
        ('de inchiriat', 'De inchiriat')
    )

    optiuni_categorii = [
        ('C0', 'Comision 0'),
        ('AR', 'Ansamblu Rezidential'),
        ('AI', 'Agentii Imobiliare')
    ]

    localitate = models.CharField(max_length=30)
    tip_proprietate = models.CharField(choices=optiuni_proprietati, max_length=30)
    tip_achizitie = models.CharField(choices=optiuni_achizitie, max_length=30)
    categorie = models.CharField(choices=optiuni_categorii, max_length=30, default='C0')

# Create your models here.
