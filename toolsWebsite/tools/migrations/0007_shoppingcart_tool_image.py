# Generated by Django 2.2 on 2020-03-28 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0006_auto_20200323_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='tool_image',
            field=models.ImageField(default='', upload_to=None),
        ),
    ]
