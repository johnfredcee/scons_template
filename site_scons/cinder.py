from SCons.Script import *

import os
import os.path
import glob
import platform

def add_opts(vars):
    vars.Add(PathVariable("CINDER_INCLUDE_PATH",
                          "Where the cinder headers live",
                          "/usr/include",
                          PathVariable.PathIsDir))
    vars.Add(PathVariable("CINDER_LIB_PATH",
                          "Where the cinder libraries live",
                          "/usr/lib/i386-linux-gnu",
                          PathVariable.PathIsDir))
    vars.Add(PathVariable("CINDER_LIB",
                          "Name of the cinder library",
                          "cinder", 0)) 
    return vars

def add_to_env(env):
    result = FindFile("Cinder.h", env["CINDER_INCLUDE_PATH"] + "/cinder/")
    if (result):
        env["CPPPATH"] += [ env["CINDER_INCLUDE_PATH"] ]
    else:
        print "Failed to find Cinder at %s " % env["CINDER_INCLUDE_PATH"] 
        Exit(1)
    lib_to_find = env.subst("${LIBPREFIX}"+env["CINDER_LIB"]+"${LIBSUFFIX}")        
    result = FindFile(lib_to_find, env["CINDER_LIB_PATH"])
    if (result):
        env["LIBS"] += [ env["CINDER_LIB"] ]
        env["LIBPATH"] += [ env["CINDER_LIB_PATH"] ]
    else:
        print "Failed to find Cinder Library %s at %s " % ( lib_to_find, env["CINDER_LIB_PATH"] )
        Exit(1)
