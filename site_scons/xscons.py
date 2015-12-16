
from SCons.Script import *

import os
import os.path
import glob
import platform
import pprint

def make_root_env(opts):
    opts.Add("PROJECT_TOOLS", "List of tools to use")
    env = Environment(variables = opts, INITIAL_ENVIRONMENT=True, tools = [])
    env.Append(BUILD_OPTIONS = opts)
    if (not("CPPPATH") in env):
        env["CPPPATH"] = []
    if (not("LIBPATH") in env):
        env["LIBPATH"] = []        
    if (not("LIBS") in env):
        env["LIBS"] = []            
    for t in env["PROJECT_TOOLS"]:
        env.Tool(t)
    return env
