# Generated by Django 5.0.7 on 2024-11-04 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_remove_scope_главный_один_scope_главный_один'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]
