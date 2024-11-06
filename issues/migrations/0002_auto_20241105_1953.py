# Generated by Django 5.1.2 on 2024-11-06 01:53

from django.db import migrations


def populate_priority(apps, schemaeditior):
    entries = {
        "low": "A low priority issue",
        "medium": "A medium priority issue",
        "high": "A high priority issue",
    }
    Priority = apps.get_model("issues", "Priority")
    for key, value in entries.items():
        priority = Priority(name=key, description=value)
        priority.save()

class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_priority),
    ]