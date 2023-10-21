# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Wrapper(object):

    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __getattr__(self, name):
        return getattr(self.wrapped, name)


class OutcomeCharacters:
    passed = '✓'
    failed = '✗'
    skipped = '»'
    default = '»'


class UTF8Wrapper(Wrapper):

    def __str__(self):
        outcome = getattr(
            OutcomeCharacters,
            self.wrapped.outcome,
            OutcomeCharacters.default)
        return ' {outcome} {node}'.format(
            outcome=outcome,
            node=self.wrapped.node
        )
