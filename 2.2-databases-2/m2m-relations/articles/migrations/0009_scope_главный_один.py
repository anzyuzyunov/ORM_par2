# Generated by Django 5.0.7 on 2024-11-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_scope_options_tag_такой_тег_уже_есть'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='scope',
            constraint=models.UniqueConstraint(condition=models.Q(('is_main', True)), fields=('tag', 'is_main'), name='главный один'),
        ),
    ]
