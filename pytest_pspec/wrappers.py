# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Wrapper(object):

    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __getattr__(self, name):
        return getattr(self.wrapped, name)


class UTF8Wrapper(Wrapper):

    _CHARACTER_BY_OUTCOME = {
        'passed': '✓',
        'failed': '✗',
        'skipped': '»',
    }

    _default_character = '»'

    def __str__(self):
        outcome = self._CHARACTER_BY_OUTCOME.get(
            self.wrapped.outcome,
            self._default_character
        )
        return ' {outcome} {node}'.format(
            outcome=outcome,
            node=self.wrapped.node
        )
