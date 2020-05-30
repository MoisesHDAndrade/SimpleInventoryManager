# Generated by Django 2.2.10 on 2020-05-13 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baixa_data', models.DateField(auto_now=True)),
                ('baixa_quantidade', models.IntegerField()),
                ('baixa_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.Produto', verbose_name='Baixa')),
            ],
        ),
    ]