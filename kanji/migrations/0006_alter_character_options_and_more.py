# Generated by Django 4.1.2 on 2022-10-16 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanji', '0005_alter_character_options_remove_character_grade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character',
            options={'ordering': ['grade']},
        ),
        migrations.RenameField(
            model_name='character',
            old_name='grades',
            new_name='grade',
        ),
    ]
