from django.db import models
from feincms import extensions


class Extension(extensions.Extension):
    def handle_model(self):
        self.model.add_to_class(
            'meta_title',
            models.CharField(
                'meta title',
                max_length=128,
                help_text='Page title tag, shown in search engines',
                blank=True)
        )
