# -*- coding: utf-8 -*-
from .__module__ import Module, dependency, source
from .python import Python
from .tensorflow import Tensorflow
from .pyopenpose import Pyopenpose
from .openpose import Openpose

@dependency(Python, Tensorflow, Pyopenpose, Openpose)
@source('apt')
class Custom_Dependencies(Module):

    def build(self):
        return r'''
            DEBIAN_FRONTEND=noninteractive apt-get update && \
            DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
                python3-tk \
                && \
            $PIP_INSTALL tflearn \
            && \
            '''
 
