# Generated by Django 3.1.3 on 2020-12-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendationsForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.CharField(max_length=100)),
                ('cuisine', models.CharField(max_length=100)),
                ('health_factor', models.CharField(max_length=100)),
                ('wait_time', models.IntegerField(null=True)),
                ('travel_time', models.IntegerField(null=True)),
                ('drive_through', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field_name', models.CharField(help_text='Enter field documentation', max_length=20)),
            ],
            options={
                'ordering': ['-my_field_name'],
            },
        ),
    ]
