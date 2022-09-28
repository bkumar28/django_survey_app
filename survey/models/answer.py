import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

from survey.models.question import Question
from survey.models.survey import Survey, SurveyInvitation


class Answer(models.Model):
    """
    An ``Answer`` stores the response by a user to a question in a survey.
    """
    invitation_id = models.ForeignKey(SurveyInvitation, related_name='answers', verbose_name=_('user'),
                                      blank=True, null=True, on_delete=models.CASCADE)
    survey_id = models.ForeignKey(Survey, related_name='answers', verbose_name=_('survey'), editable=False,
                                  on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, related_name='answers', verbose_name=_('question'),
                                    on_delete=models.CASCADE)
    ans = models.TextField(_('Answer'), max_length=2048, blank=True)
    submit_date = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        db_table = 'answers'

    def __str__(self):
        return "{0} : {1}".format(self.survey_id.title, self.question_id.title)
