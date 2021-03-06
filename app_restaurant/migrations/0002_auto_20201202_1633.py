# Generated by Django 3.1.3 on 2020-12-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['-name']},
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='my_field_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='cost',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='cuisine',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='drive_through',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='health_factor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='travel_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='wait_time',
            field=models.IntegerField(null=True),
        ),
    ]
