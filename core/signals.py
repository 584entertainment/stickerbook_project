from django.db.models.signals import pre_delete
from django.dispatch import receiver
from core.models import Teacher, Student

@receiver(pre_delete, sender=Teacher)
def reassign_students_to_default(sender, instance, **kwargs):
    """Reassign students to the default teacher when their teacher is deleted."""
    default_teacher = Teacher.objects.get(user__username="default_teacher")
    Student.objects.filter(teacher=instance).update(teacher=default_teacher)

