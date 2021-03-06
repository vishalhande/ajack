# Generated by Django 3.0.10 on 2020-09-14 11:41

import ajackapp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.CharField(max_length=300)),
                ('summary', models.CharField(max_length=60)),
                ('document', models.FileField(upload_to='pdf')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catref', to='ajackapp.Content')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField(validators=[ajackapp.models.phone_validation], verbose_name='phone')),
                ('address', models.CharField(max_length=300, verbose_name='address')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('state', models.CharField(max_length=50, verbose_name='state')),
                ('country', models.CharField(max_length=50, verbose_name='country')),
                ('pincode', models.IntegerField(validators=[ajackapp.models.pincode_validation], verbose_name='pincode')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
