# -*- coding: utf-8 -*-
from .__module__ import Module, dependency, source
from .python import Python
from .tensorflow import Tensorflow
from .pyopenpose import Pyopenpose
from .openpose import Openpose
from .keras import Keras


@dependency(Python, Tensorflow, Pyopenpose, Openpose, Keras)
@source('apt')
class Custom_Dependencies(Module):

    def build(self):
        return r'''
            DEBIAN_FRONTEND=noninteractive apt-get update && \
            DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
                mesa-common-dev \
                libglu1-mesa-dev \ 
                python3-tk \
                && \
            $PIP_INSTALL pyqt5 \
            && \
            '''
 
