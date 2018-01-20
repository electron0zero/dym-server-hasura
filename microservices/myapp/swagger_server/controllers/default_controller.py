import connexion
from swagger_server.models.inline_response200 import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from .core import segment_and_correct


def dym_get(payload, spell, segment):
    """
    does spell correction and word segmentation on payload.
    See more [Spell Checker](https://en.wikipedia.org/wiki/Spell_checker), [Text Segmentation](https://en.wikipedia.org/wiki/Text_segmentation)
    :param payload: Payload
    :type payload: str
    :param spell: Do/Don&#39;t Spelling Correction on payload
    :type spell: bool
    :param segment: Do/Don&#39;t word segmentation on payload
    :type segment: bool

    :rtype: InlineResponse200
    """
    return segment_and_correct(payload, spelling=spell, segmenting=segment)


def dym_post(payload, spell, segment):
    """
    does spell correction and word segmentation on payload.
    See more [Spell Checker](https://en.wikipedia.org/wiki/Spell_checker), [Text Segmentation](https://en.wikipedia.org/wiki/Text_segmentation)
    :param payload: Payload
    :type payload: str
    :param spell: Do/Don&#39;t Spelling Correction on payload
    :type spell: bool
    :param segment: Do/Don&#39;t word segmentation on payload
    :type segment: bool

    :rtype: InlineResponse200
    """
    return segment_and_correct(payload, spelling=spell, segmenting=segment)
