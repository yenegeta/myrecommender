# Generated by Django 2.2.2 on 2019-07-07 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('artist', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUserAdmin',
        ),
    ]
