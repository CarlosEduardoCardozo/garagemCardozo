# Generated by Django 4.2.1 on 2023-05-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0005_alter_cor_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
    ]