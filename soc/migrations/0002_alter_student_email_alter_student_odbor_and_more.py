# Generated by Django 4.2.13 on 2024-06-07 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='odbor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='priezvisko',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tema',
            name='dostupnost',
            field=models.CharField(choices=[('Voľne', 'Voľne'), ('Čaká na schválenie', 'Čaká na schválenie'), ('Obsadené', 'Obsadené')], max_length=300),
        ),
        migrations.AlterField(
            model_name='tema',
            name='nazov',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ucitel',
            name='meno',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ucitel',
            name='priezvisko',
            field=models.CharField(max_length=30),
        ),
    ]
