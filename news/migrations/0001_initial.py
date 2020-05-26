# Generated by Django 3.0.6 on 2020-05-26 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Giornalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('cognome', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Articolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100)),
                ('contenuto', models.TextField()),
                ('giornalista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articoli', to='news.Giornalista')),
            ],
        ),
    ]
