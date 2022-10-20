# Generated by Django 4.1.2 on 2022-10-16 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.CharField(choices=[('first', 'first'), ('second', 'second'), ('third', 'third'), ('fourth', 'fourth'), ('fifth', 'fifth'), ('sixth', 'sixth'), ('seventh', 'seventh')], default=('first', 'first'), max_length=7),
        ),
    ]