# Generated by Django 4.2.1 on 2023-06-08 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_users_type_password_users_type_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tur',
            name='count',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=15, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
