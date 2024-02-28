from django.db import models

# Create your models here.
class Anunt(models.Model):


    optiuni_proprietati = [
        ('apartamente', 'Apartamente'),
        ('case/vile', 'Case/Vile'),
        ('terenuri', 'Terenuri')
    ]

    optiuni_achizitie = [
        ('de vanzare', 'De vanzare'),
        ('de inchiriat', 'De inchiriat')
    ]

    tipuri_anunt = [
        ('C0', 'Comision 0'),
        ('AR', 'Ansamblu Rezidential'),
        ('AI', 'Agentii Imobiliare')
    ]

    tip_proprietate = models.CharField(choices=optiuni_proprietati, max_length=30)
    tip_vanzare = models.CharField(choices=optiuni_achizitie, max_length=30)
    titul_anunt = models.CharField(max_length=80)
    poze = models.ImageField(upload_to='media/', null=True)
    suprafata_utila = models.CharField(max_length=10)
    numar_camere = models.CharField(max_length=15)
    numar_bai = models.CharField(max_length=15)
    numar_carte_funciara = models.CharField(max_length= 15)
    pret = models.CharField(max_length=30)
    localizare = models.CharField(max_length=80)
    descriere = models.TextField(max_length=500)
    tip_anunt = models.CharField(choices=tipuri_anunt, max_length=2)

class Promovare(models.Model):

    tipuri_promovare = [
        ('SP', 'Promovare Simpla'),
        ('PP', 'Promovare Premium'),
        ('TL', 'Top Listing')
    ]

    metoda_de_promovare = models.CharField(choices=tipuri_promovare, max_length=2, default="SP")
    anunt = models.ForeignKey(Anunt, on_delete=models.CASCADE)

