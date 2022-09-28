from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

SURVEY_STATUS_CHOICES = (
    ('D', 'Draft'),
    ('S', 'Started')
)


class Survey(models.Model):
    """
    A ``Survey`` is the activity of gathering answers based on a question.
    """
    title = models.CharField(_('Title'), max_length=120, )
    description = models.TextField(verbose_name=_("description"), blank=True)
    start_date = models.DateTimeField(_('Starts accepting submissions date'), null=True)
    expired_date = models.DateTimeField(_('Stops accepting submissions date'), null=True)
    status = models.CharField(_('Status'), max_length=1, choices=SURVEY_STATUS_CHOICES, default=1)

    created_by = models.ForeignKey(User, related_name="+", on_delete=models.PROTECT, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name="+", on_delete=models.PROTECT, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField("Updated On", blank=True, null=True)

    class Meta:
        db_table = 'surveys'

    def __str__(self):
        return self.title


class SurveyInvitation(models.Model):
    survey_id = models.ForeignKey(Survey, related_name='invitation', verbose_name=_('survey'), editable=False,
                                  on_delete=models.CASCADE)
    email = models.EmailField(max_length=256, blank=True)
    user_id = models.ForeignKey(User, related_name='invitation', verbose_name=_('user'), blank=True, null=True,
                                on_delete=models.PROTECT)

    class Meta:
        db_table = 'survey_invitations'

    def __str__(self):
        if self.email != "":
            return "{0} : {1}".format(self.survey_id.title, self.email)
        elif self.user_id is not None:
            return "{0} : {1}".format(self.survey_id.title, self.user_id.first_name)
        else:
            return "{0".format(self.survey_id.title)