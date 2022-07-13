# Generated by Django 4.0.5 on 2022-07-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0008_alter_setting_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на facebook'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на instagram'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на twitter'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на youtube'),
        ),
    ]
