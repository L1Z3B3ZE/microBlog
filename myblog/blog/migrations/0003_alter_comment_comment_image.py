# Generated by Django 4.2.5 on 2023-12-15 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_user_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_image',
            field=models.ImageField(blank=True, null=True, upload_to='comment_image/', verbose_name='Фотография'),
        ),
    ]
