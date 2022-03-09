# Generated by Django 4.0.3 on 2022-03-09 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('modelo', models.CharField(max_length=30)),
                ('kmRodados', models.CharField(max_length=30)),
                ('ano', models.PositiveIntegerField()),
                ('cor', models.CharField(max_length=30)),
                ('tipo_combustivel', models.CharField(choices=[('G', 'Gasolina'), ('A', 'Alcool'), ('D', 'Diesel'), ('E', 'Eletrico'), ('F', 'Flex')], max_length=1)),
                ('descricao', models.TextField(max_length=255)),
                ('baiiro', models.CharField(max_length=60)),
                ('rua', models.CharField(max_length=60)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='plataforma.cidade')),
                ('imagens', models.ManyToManyField(to='plataforma.imagem')),
            ],
        ),
    ]
