#!/usr/bin/env python
# encoding: utf-8

from ycyc.base.shelltools import ShellCommands
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'update the database models'

    def handle(self, *args, **options):
        status = ShellCommands.python.check_call(
            "manage.py", "makemigrations",
        )
        if status != 0:
            return status
        return ShellCommands.python.check_call(
            "manage.py", "migrate",
        )
