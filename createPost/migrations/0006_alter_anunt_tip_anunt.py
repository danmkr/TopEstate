# Generated by Django 5.0 on 2023-12-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createPost', '0005_alter_anunt_numar_carte_funciara'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anunt',
            name='tip_anunt',
            field=models.CharField(choices=[('C0', 'Comision 0'), ('AR', 'Ansamblu Rezidential'), ('AI', 'Agentii Imobiliare')], max_length=2),
        ),
    ]