# pylint: disable=C0111,R0903

"""Displays the current time, using the optional format string as input for strftime."""

from __future__ import absolute_import
import datetime
import bumblebee.engine

def default_format(module):
    default = "%x %X"
    if module == "date":
        default = "%x"
    if module == "time":
        default = "%X"
    return default

class Module(bumblebee.engine.Module):
    def __init__(self, engine):
        super(Module, self).__init__(engine,
            bumblebee.output.Widget(full_text=self.get_time)
        )
        module = self.__module__.split(".")[-1]

        self._fmt = default_format(module)

#        self._fmt = self._config.parameter("format", default_format(module))

    def get_time(self):
        return datetime.datetime.now().strftime(self._fmt)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
