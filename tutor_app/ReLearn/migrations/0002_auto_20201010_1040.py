# Generated by Django 3.1 on 2020-10-10 02:40

from django.db import migrations

def create_data(apps, schema_editor):
    ReLearn = apps.get_model('user', 'ReLearn')
    ReLearn(user_name="TEST USER", user_type="1", user_personality="XXXX", user_writeup = "TEST DESCRIPTION")
class Migration(migrations.Migration):

    dependencies = [
        ('ReLearn', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='ReLearn',
        ),

        migrations.RunPython(create_data),
    ]
