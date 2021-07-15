# Generated by Django 3.1.1 on 2020-09-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='donorform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='donorlist',
        ),
    ]