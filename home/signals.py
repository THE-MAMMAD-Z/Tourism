import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Place
from datetime import datetime

@receiver(post_save, sender=Place)
def log_place_creation(sender, instance, created, **kwargs):
    if created:
        log_message = f"Place Created: {instance.name}, Created at: {datetime.now()}\n"
        log_file_path = os.path.join(os.path.dirname(__file__), 'Place_log.txt')

        with open(log_file_path, 'a') as log_file:
            log_file.write(log_message)

@receiver(post_delete, sender=Place)
def log_place_deletion(sender, instance, **kwargs):
    log_message = f"Place Deleted: {instance.title}, Deleted at: {datetime.now()}\n"
    log_file_path = os.path.join(os.path.dirname(__file__), 'Place_log.txt')

    with open(log_file_path, 'a') as log_file:
        log_file.write(log_message)