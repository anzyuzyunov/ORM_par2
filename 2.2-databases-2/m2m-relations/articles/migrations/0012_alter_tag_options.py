# Generated by Django 5.0.7 on 2024-11-05 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]
