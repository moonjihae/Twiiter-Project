# Generated by Django 2.2 on 2019-07-22 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20190718_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
