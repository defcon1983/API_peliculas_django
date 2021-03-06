# Generated by Django 2.1.7 on 2019-02-26 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeliculaFavorita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='pelicula',
            options={'ordering': ['titulo']},
        ),
        migrations.AddField(
            model_name='peliculafavorita',
            name='pelicula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Pelicula'),
        ),
        migrations.AddField(
            model_name='peliculafavorita',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
