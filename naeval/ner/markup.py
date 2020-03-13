
from ipymarkup.ner import show_ner_line_markup as show_markup_
from ipymarkup.palette import BLUE, palette

from naeval.record import Record
from naeval.span import Span
from naeval.sent import (
    sentenize,
    sent_spans
)


class Markup(Record):
    __attributes__ = ['text', 'spans']
    __annotations__ = {
        'spans': [Span]
    }

    label = None

    def __init__(self, text, spans):
        self.text = text
        self.spans = spans

    @property
    def sents(self):
        cls = self.__class__
        for sent in sentenize(self.text):
            spans = sent_spans(sent, self.spans)
            yield cls(sent.text, list(spans))

    @property
    def adapted(self):
        raise NotImplementedError


def show_markup(text, spans):
    show_markup_(text, spans, palette=palette(BLUE))
