from django.db import migrations


def add_rewards(apps, schema_editor):
    Reward = apps.get_model('rewards', 'Reward')
    db_alias = schema_editor.connection.alias

    Reward.objects.using(db_alias).create(
        name="Tote Bag of Holding",
        description="Tote bag emblazoned with Django logo that magically expands to accommodate all the swag you collect.",
        point_value=2.75
    )
    Reward.objects.using(db_alias).create(
        name="Potion of Endless Coffee",
        description="A tiny vial that, when opened, releases the invigorating aroma of freshly brewed coffee.",
        point_value=2.25
    )
    Reward.objects.using(db_alias).create(
        name="Wand of Presentation",
        description="Wield to advance, pause, or rewind presentation slides.",
        point_value=1.5
    )
    Reward.objects.using(db_alias).create(
        name="Mimic Mouse Pad",
        description="A perfectly ordinary mouse pad. Right...? It is just a mouse pad, isn't it?",
        point_value=2
    )
    Reward.objects.using(db_alias).create(
        name="Scroll of Infinite WiFi",
        description="When unfurled, creates a area of super-fast secure WiFi for you and your companions.",
        point_value=3.75
    )
    Reward.objects.using(db_alias).create(
        name="T-Shirt +2",
        description="Official DjangoCon 2023 T-shirt, +2 to Armor Class.",
        point_value=2
    )


def remove_rewards(apps, schema_editor):
    Reward = apps.get_model('rewards', 'Reward')
    db_alias = schema_editor.connection.alias
    Reward.objects.all().using(db_alias).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('rewards', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_rewards, remove_rewards),

    ]
