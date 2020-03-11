# Generated by Django 3.0.2 on 2020-02-14 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToolCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('count', models.IntegerField(default=0)),
                ('unavailable', models.IntegerField(default=0)),
            ],
        ),
    ]