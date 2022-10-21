# Generated by Django 4.1.2 on 2022-10-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.CharField(choices=[('1', 'first'), ('2', 'second'), ('3', 'third'), ('4', 'fourth'), ('5', 'fifth'), ('6', 'sixth'), ('7', 'seventh')], default=('1', 'first'), max_length=7),
        ),
    ]