# Generated by Django 4.1.10 on 2023-07-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pic', models.ImageField(blank=True, null=True, upload_to='User/Porfile/%Y/%m/%d')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
    ]