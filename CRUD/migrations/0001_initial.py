# Generated by Django 3.1.7 on 2021-03-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateField()),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
