from SCons.Script import *

import os
import os.path
import glob
import platform


def exists(env):
    return True

def generate(env, **kwargs):
    vars = env["BUILD_OPTIONS"]
    vars.Add(PathVariable("GLEW_INCLUDE_PATH",
                          "Where the glew headers live",
                          "/usr/include"))
    vars.Add(PathVariable("GLEW_LIB_PATH",
                          "Where the glew library lives",
                          "/usr/lib/i386-linux-gnu",
                          PathVariable.PathIsDir))
    glewenv = Environment(variables = vars, tools = [])
    env.Append(GLEW_INCLUDE_PATH = glewenv["GLEW_INCLUDE_PATH"])
    env.Append(GLEW_LIB_PATH = glewenv["GLEW_LIB_PATH"])
    result = FindFile("glew.h", env["GLEW_INCLUDE_PATH"] + "/GL")
    if (result):
        if (not("CPPPATH" in env) or (not(env["GLEW_INCLUDE_PATH"] in env["CPPPATH"]))):
            env.Append(CPPPATH = env["GLEW_INCLUDE_PATH"])
        else:
            pass
    else:
        print "Failed to find glew at %s " % ( env["GLEW_INCLUDE_PATH"] )
        Exit(1)
    lib_to_find = env.subst("${SHLIBPREFIX}"+"GLEW"+"${SHLIBSUFFIX}")            
    result = FindFile(lib_to_find, env["GLEW_LIB_PATH"])
    if (result):
        if (not("LIBPATH" in env) or (not(env["GLEW_LIB_PATH"] in env["LIBPATH"]))):
            env.Append(LIBPATH  = env["GLEW_LIB_PATH"])
            env.Append(LIBS =  [ "GLEW" ])
    else:
        print "Failed to find glew %s library at %s " % ( lib_to_find, env["GLEW_LIB_PATH"] )
        Exit(1)                            
    return env
    
