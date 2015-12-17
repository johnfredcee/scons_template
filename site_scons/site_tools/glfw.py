from SCons.Script import *

import os
import os.path
import glob
import platform


def exists(env):
    return True

def generate(env, **kwargs):
    vars = env["BUILD_OPTIONS"]
    vars.Add(PathVariable("GLFW_INCLUDE_PATH",
                          "Where the glfw headers live",
                          "/usr/include"))
    vars.Add(PathVariable("GLFW_LIB_PATH",
                          "Where the glfw library lives",
                          "/usr/lib/i386-linux-gnu",
                          PathVariable.PathIsDir))
    glfwenv = Environment(variables = vars, tools = [])
    env.Append(GLFW_INCLUDE_PATH = glfwenv["GLFW_INCLUDE_PATH"])
    env.Append(GLFW_LIB_PATH = glfwenv["GLFW_LIB_PATH"])
    result = FindFile("glfw3.h", env["GLFW_INCLUDE_PATH"]  + "/GLFW")
    if (result):
        if (not("CPPPATH" in env) or (not(env["GLFW_INCLUDE_PATH"] in env["CPPPATH"]))):
            env.Append(CPPPATH =  env["GLFW_INCLUDE_PATH"])
        else:
            pass
    else:
        print "Failed to find glfw at %s " % ( env["GLFW_INCLUDE_PATH"] )
        Exit(1)
    lib_to_find = env.subst("${LIBPREFIX}"+"glfw3"+"${LIBSUFFIX}")            
    result = FindFile(lib_to_find, env["GLFW_LIB_PATH"])
    if (result):
        if (not("LIBPATH" in env) or (not(env["GLFW_LIB_PATH"] in env["LIBPATH"]))):
            env.Append(LIBPATH = env["GLFW_LIB_PATH"])
            env.Append(LIBS =  [ "glfw3" ])
    else:
        print "Failed to find glfw %s library at %s " % ( lib_to_find, env["GLFW_LIB_PATH"] )
        Exit(1)                            
    return env
    
