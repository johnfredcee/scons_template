# Copyright (C) 2015 John Connors.

import os
import platform
from SCons.Defaults import *
#
# The xscons module will define what variables the project
# expects to be set in a options_<platform>.py file. Right now
# this is set up to use the Visual C++ Build tools in Windows,
# rather than the usual Visual Studio compilers
#
import xscons

#
# This SConstruct is deliberately miniamalistic
# It loads a file called options_<platformname>.py in the same directory
# as the SConstruct. The options file defines the variables that affect the
# build, such as the locations of tools, includes and such.
#
optfile = "options_"+platform.system().lower()+".py"
print("Looking for options in " + optfile)
vars = Variables(optfile)
env = xscons.make_root_env(vars);
env.Program("hello_boost", [ "hello_boost.cpp" ])
