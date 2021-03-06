# Generated by Django 3.2 on 2021-06-08 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_guitarra_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesorio',
            name='imagen',
            field=models.ImageField(null=True, upload_to='accesorio'),
        ),
        migrations.AddField(
            model_name='amplificador',
            name='imagen',
            field=models.ImageField(null=True, upload_to='amplificador'),
        ),
        migrations.AddField(
            model_name='bajo',
            name='imagen',
            field=models.ImageField(null=True, upload_to='bajo'),
        ),
        migrations.AddField(
            model_name='percusion',
            name='imagen',
            field=models.ImageField(null=True, upload_to='percusion'),
        ),
        migrations.AddField(
            model_name='piano',
            name='imagen',
            field=models.ImageField(null=True, upload_to='piano'),
        ),
    ]
