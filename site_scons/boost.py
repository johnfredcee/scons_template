from SCons.Script import *

import os
import os.path
import glob
import platform


def add_opts(vars):
    print dir(vars.Add)
    vars.Add(PathVariable("BOOST_INCLUDE_PATH",
                          "Where the boost headers live",
                          "/usr/include",
                          PathVariable.PathIsDir))
    vars.Add(PathVariable("BOOST_LIB_PATH",
                          "Where the boost library lives",
                          "/usr/lib/i386-linux-gnu",
                          PathVariable.PathIsDir))
    vars.Add(ListVariable("BOOST_LIBRARIES",
                          "Boost Libraires to link",
                          'all',
                          [ "atomic", "filesystem", "chrono", "context", "coroutine",
                            "date_time", "exception", "iostreams", "locale", "log",
                            "math", "python", "random", "regex", "signals", "system", "thread",
                            "timer", "wave" ]))
    return vars

def add_to_env(env):
    result = FindFile("version.hpp", env["BOOST_INCLUDE_PATH"] + "/boost")
    if (result):
        if (not(env["BOOST_INCLUDE_PATH"] in env["CPPPATH"])):
            env["CPPPATH"] += [ env["BOOST_INCLUDE_PATH"] ]
        else:
            pass
    else:
        print "Failed to find boost at %s " % ( env["BOOST_INCLUDE_PATH"] )
        Exit(1)
    if ("BOOST_LIBRARIES" in env):
        for boost_lib in env["BOOST_LIBRARIES"]:
            lib_to_find = env.subst("${LIBPREFIX}boost_"+boost_lib+"${LIBSUFFIX}")
            result = FindFile(lib_to_find, env["BOOST_LIB_PATH"])
            if (result):
                if (not(env["BOOST_LIB_PATH"] in env["LIBPATH"])):
                    env["LIBPATH"] += [ env["BOOST_LIB_PATH"] ]
                env["LIBS"] +=  [ "boost_" + boost_lib ]
            else:
                print "Failed to find boost %s library at %s " % ( boost_lib, env["BOOST_LIB_PATH"] )
                Exit(1)                            
    return env
    
