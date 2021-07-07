# Generated by Django 3.0.7 on 2021-07-03 20:47

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0012_liveschedule_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('color', colorfield.fields.ColorField(default='#ff0000', max_length=18)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='works.Work'),
        ),
        migrations.AlterField(
            model_name='work',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='works', to='works.Genre'),
        ),
        migrations.AddField(
            model_name='work',
            name='tags',
            field=models.ManyToManyField(to='works.Tag'),
        ),
    ]