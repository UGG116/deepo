# -*- coding: utf-8 -*-
from .__module__ import Module, dependency, source
from .python import Python
from .boost import Boost
from .openpose import Openpose


@dependency(Boost, Openpose)
@source('git')
class Pyopenpose(Module):

    def build(self):
        return r'''
            $GIT_CLONE https://github.com/christian-lanius/PyOpenPose.git /software/pyopenpose && \
            export OPENPOSE_ROOT=/software/openpose && \
            cd /software/pyopenpose && \
            mkdir build && \
            cd build && \
            cmake .. && \
            make && \
            export PYTHONPATH=$PYTHONPATH:/software/pyopenpose/build/PyOpenPoseLib && \
        '''

