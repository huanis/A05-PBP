# Generated by Django 3.2.7 on 2021-10-28 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentHealthy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentator_name', models.CharField(default='', max_length=100, null=True)),
                ('comment_field', models.TextField(default='')),
            ],
        ),
    ]
