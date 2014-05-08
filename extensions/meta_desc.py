from django.db import models
from feincms import extensions


class Extension(extensions.Extension):
    def handle_model(self):
        self.model.add_to_class(
            'meta_desc',
            models.TextField(
                'meta description',
                help_text='Meta description for the page shown in search engines',
                blank=True)
        )