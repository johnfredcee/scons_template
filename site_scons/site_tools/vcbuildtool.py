
#
# This estabilshes the VC Build tools as a build option on Windows
#
from SCons.Script import *

def exists(env):
    return True
    
def generate(env, **kwargs):
    opts = env["BUILD_OPTIONS"]
    opts.Add(PathVariable("VC_BUILD_TOOLS_PATH", "Where the VC++ Build tools are installed", "C:/Program Files (x86)/Microsoft Visual C++ Build Tools", PathVariable.PathIsDir))
    msenv = Environment(tools = [], variables=opts)
    env.Append(MSVC_USE_SCRIPT = msenv["VC_BUILD_TOOLS_PATH"] + "/vcbuildtools.bat")
    env.Tool("msvc")
    env.Tool("mslink")
    env.Tool("mslib")
