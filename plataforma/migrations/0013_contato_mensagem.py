# Generated by Django 4.0.3 on 2022-03-10 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0012_contato'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mensagem',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
