# Generated by Django 2.0.3 on 2018-03-28 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagxreceta',
            name='receta',
        ),
        migrations.RemoveField(
            model_name='tagxreceta',
            name='tag',
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='receta',
            name='calificacion',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='receta',
            name='cantidad_calificaciones',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='receta',
            name='porciones',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='TagXReceta',
        ),
    ]
