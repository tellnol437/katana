# -*- coding: utf-8 -*-
# @Author: John Hammond
# @Date:   2019-02-28 22:33:18
# @Last Modified by:   John Hammond
# @Last Modified time: 2019-03-31 16:06:53

from pwn import *
from unit import BaseUnit
import os

class EsotericUnit(BaseUnit):

    @classmethod
    def prepare_parser(cls, config, parser):
        # Nothing to really do with this "raw file" unit...
        # At least that I can think of at the moment.
        pass


    def __init__(self, config):
        super(EsotericUnit, self).__init__(config)


    # The sub-class should define this, to see if the action is feasible...
    def check(self, target):
        return True

        # We could check if this is a file, but if it's not...
        # if ( os.path.exists(target) ):
        #     return True
        # else:
        #     log.failure("%s does not exist!" % target )
        #     return False


    # The sub-class should define this...
    #  def evaluate(self, target):
    #     pass  
    #
    # If you do not include this function, the main unit.py
    # will properly display its name.