from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
# Get_all_lexers returns in format (name, (alias,), ....) we just want name & first alias
lang_name, alias, first_alias = 0, 1, 0
# choices -> list[tuple] -> tuple[0] -> actual value, tuple[1] -> human readable name
LANGUAGE_CHOICES = sorted([(item[alias][first_alias], item[lang_name]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles() if item])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    lineos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.title
