# Generated by Django 5.2.3 on 2025-06-15 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["-created_at"]},
        ),
        migrations.RenameField(
            model_name="task",
            old_name="CREATED_AT",
            new_name="created_at",
        ),
    ]
