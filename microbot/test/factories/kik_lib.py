# coding=utf-8
from kik.messages import TextMessage
from factory import Sequence, Factory
from factory.fuzzy import FuzzyText
from django.utils import timezone
import uuid

class KikMessageLibFactory(Factory):
    class Meta:
        model = TextMessage
    id = uuid.uuid4()
    from_user = Sequence(lambda n: 'username_%d' % n)
    timestamp = timezone.now()
    chat_id = Sequence(lambda n: 'chat_id_%d' % n)
    body = FuzzyText()    