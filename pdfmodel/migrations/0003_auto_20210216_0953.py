# Generated by Django 3.1.5 on 2021-02-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfmodel', '0002_customerpdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerpdf',
            name='pdf_file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='media'),
        ),
    ]