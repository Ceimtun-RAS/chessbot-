# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/usr/local/Caskroom/miniforge/base/envs/ros-noetic-tools/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/usr/local/Caskroom/miniforge/base/envs/ros-noetic-tools/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/usr/local/Caskroom/miniforge/base/envs/ros-noetic-tools'.split(';'):
        python_path = os.path.join(workspace, 'lib/python3.9/site-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/Users/amoralesma/Documents/ieee-un/Proyectos/chessbot-controller/chessbot_ws/devel/.private/catkin_tools_prebuild/env.sh')

output_filename = '/Users/amoralesma/Documents/ieee-un/Proyectos/chessbot-controller/chessbot_ws/build/catkin_tools_prebuild/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
