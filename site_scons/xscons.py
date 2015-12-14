
from SCons.Script import *

import os
import os.path
import glob
import platform
import boost

def make_root_env(opts):
    boost.add_opts(opts)
    env = Environment(variables = opts)
    if (not("CPPPATH") in env):
        env["CPPPATH"] = []
    if (not("LIBPATH") in env):
        env["LIBPATH"] = []        
    if (not("LIBS") in env):
        env["LIBS"] = []        
    boost.add_to_env(env)
    return env
