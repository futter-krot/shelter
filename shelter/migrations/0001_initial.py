# Generated by Django 2.2.6 on 2021-04-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('found', models.DateTimeField(auto_now_add=True)),
                ('atype', models.PositiveSmallIntegerField(choices=[(0, 'Unknown'), (1, 'Cat'), (2, 'Dog'), (3, 'Parrot')], default=0, verbose_name='animal type')),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
