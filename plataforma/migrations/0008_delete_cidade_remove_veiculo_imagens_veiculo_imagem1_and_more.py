# Generated by Django 4.0.3 on 2022-03-09 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0007_alter_veiculo_cidade'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cidade',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='imagens',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='imagem1',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='veiculo',
            name='imagem2',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='veiculo',
            name='imagem3',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Imagem',
        ),
    ]
