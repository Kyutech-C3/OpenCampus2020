# Generated by Django 3.0.7 on 2020-07-16 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0010_auto_20200716_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='works.Game'),
        ),
        migrations.AlterField(
            model_name='work',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='works.Genre'),
        ),
        migrations.AlterField(
            model_name='work',
            name='model3d',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='works.Model3D'),
        ),
        migrations.AlterField(
            model_name='work',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='works.Video'),
        ),
    ]
