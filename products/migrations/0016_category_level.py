from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20190328_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='level',
            field=models.PositiveSmallIntegerField(default=0, editable=False,
                                                   help_text='Resembles the level in the tree.'),
        ),
    ]
