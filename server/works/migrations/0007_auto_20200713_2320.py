# Generated by Django 3.0.7 on 2020-07-13 23:20

from django.db import migrations, models
import works.validators


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0006_auto_20200712_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='mp4',
            field=models.FileField(default='default.mp4', upload_to='videos/', validators=[works.validators.validate_is_mp4]),
            preserve_default=False,
        ),
    ]