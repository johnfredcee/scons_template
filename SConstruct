import os
import platform
from SCons.Defaults import *
import xscons


optfile = "options_"+platform.system().lower()+".py"
print "Looking for options in ", optfile
vars = Variables(optfile)
env = xscons.make_root_env(vars);
env.Program("hello_boost", [ "hello_boost.cpp" ])
