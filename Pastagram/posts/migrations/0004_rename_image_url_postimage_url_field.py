# Generated by Django 4.2.5 on 2024-01-12 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_postimage_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postimage',
            old_name='image_url',
            new_name='url_field',
        ),
    ]