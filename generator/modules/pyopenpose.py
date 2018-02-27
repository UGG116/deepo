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
            $GIT_CLONE https://github.com/FORTH-ModelBasedTracker/PyOpenPose.git /pyopenpose && \
            export OPENPOSE_ROOT=/openpose && \
            sed -i 's@find_package(PythonLibs 2.7 EXACT REQUIRED)@#find_package(PythonLibs 2.7 EXACT REQUIRED)@g' /pyopenpose/CMakeLists.txt && \
            sed -i 's/#find_package(Boost COMPONENTS system python-py35 REQUIRED)/find_package(Boost COMPONENTS system python3 REQUIRED)/g' /pyopenpose/CMakeLists.txt && \
            sed -i 's/find_package(Boost COMPONENTS system python-py27 REQUIRED)/#find_package(Boost COMPONENTS system python-py27 REQUIRED)/g' /pyopenpose/CMakeLists.txt && \
            sed -i 's/#find_package(PythonLibs 3 EXACT REQUIRED)/find_package(PythonLibs 3 EXACT REQUIRED)/g' /pyopenpose/CMakeLists.txt && \
            mkdir -p /pyopenpose/build && cd /pyopenpose/build && \
            cmake .. && \
            make && \
        '''

