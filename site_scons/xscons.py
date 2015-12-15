
from SCons.Script import *

import os
import os.path
import glob
import platform
import boost
import cinder

def make_root_env(opts):
    opts.Add("TOOLS", "List of tools to use")
    boost.add_opts(opts)
    cinder.add_opts(opts)
    env = Environment(variables = opts, tools = [])
    for t in env["TOOLS"]:
        env.Tool(t, xsconsopts = opts)
    if (not("CPPPATH") in env):
        env["CPPPATH"] = []
    if (not("LIBPATH") in env):
        env["LIBPATH"] = []        
    if (not("LIBS") in env):
        env["LIBS"] = []        
    boost.add_to_env(env)
    cinder.add_to_env(env)
    return env
