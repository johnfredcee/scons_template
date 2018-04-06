
#
# This is the script that establises the cross-platform build environment and
# what option variables we specify in an options file
#
from SCons.Script import *

import os
import os.path
import glob
import platform
import pprint

def make_root_env(opts):
    opts.Add("PROJECT_TOOLS", "List of tools to use")
    opts.Add("PROJECT_CPPPATH", "Extra include paths for project", [])
    opts.Add("PROJECT_CCFLAGS", "Extra C flags for project", [])
    opts.Add("PROJECT_CXXFLAGS", "Extra C++ flags for project", [])
    opts.Add("PROJECT_LIBPATH", "Extra library paths for project", [])
    opts.Add("PROJECT_LIBS", "Extra libraries for project", [])
    env = Environment(variables = opts, INITIAL_ENVIRONMENT=True, tools = [])
    env["CPPPATH"] = []
    env.Append(BUILD_OPTIONS = opts)
    for t in env["PROJECT_TOOLS"]:
        env.Tool(t)
    env.Append(CPPPATH = env["PROJECT_CPPPATH"])
    env.Append(LIBPATH  = env["PROJECT_LIBPATH"])
    env.Append(CCFLAGS = env["PROJECT_CCFLAGS"])
    env.Append(CXXFLAGS = env["PROJECT_CXXFLAGS"])        
    env.Append(LIBS = env["PROJECT_LIBS"])        
    return env
