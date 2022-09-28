from django.db import models
from django.utils.translation import ugettext_lazy as _

from survey.models.survey import Survey

FIELD_TYPE_CHOICES = (
    ('T', 'Text Input'),
    ('N', 'Number'),
)


class Question(models.Model):
    title = models.CharField(_('Title'), max_length=80)
    survey_id = models.ForeignKey(Survey, related_name='questions', verbose_name=_('survey'), on_delete=models.CASCADE)
    field_type = models.CharField(_('Field type'), max_length=2, choices=FIELD_TYPE_CHOICES)
    is_required = models.BooleanField(_('Is Required'), default=True)

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return "{0} : {1}".format(self.survey_id.title, self.title)
