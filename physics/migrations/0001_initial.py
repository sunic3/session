# Generated by Django 3.0.1 on 2020-01-12 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
                'ordering': ['num'],
            },
        ),
        migrations.CreateModel(
            name='PhysImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='physics/')),
                ('pos', models.IntegerField()),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='physics.Ticket')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'ordering': ['ticket__num', 'pos'],
            },
        ),
    ]
