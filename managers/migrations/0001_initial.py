# Generated by Django 2.2.14 on 2020-11-25 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=200)),
            ],
        ),
    ]