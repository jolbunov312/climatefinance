# Generated by Django 3.0 on 2023-09-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climatefinance', '0002_auto_20230903_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.CharField(default='https://geekflare.com/wp-content/uploads/2023/03/img-placeholder.png', max_length=500),
        ),
    ]
