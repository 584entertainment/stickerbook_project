from django.db import migrations

def create_default_teacher(apps, schema_editor):
    Teacher = apps.get_model('core', 'Teacher')
    User = apps.get_model('auth', 'User')
    School = apps.get_model('core', 'School')

    # Create a school for the default teacher
    school, _ = School.objects.get_or_create(name="Default School", defaults={'end_of_school_time': "15:00"})
    user, _ = User.objects.get_or_create(username="default_teacher", defaults={'password': "password123"})

    # Create the default teacher
    Teacher.objects.get_or_create(user=user, name="Default Teacher", school=school)

class Migration(migrations.Migration):
    dependencies = [
        ('core', 'previous_migration_name'),  # Replace with the name of the previous migration
    ]

    operations = [
        migrations.RunPython(create_default_teacher),
    ]
