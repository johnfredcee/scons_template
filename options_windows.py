# These are the tools we pull from ./site_scons/site_tools for building the program on this platform
#PROJECT_TOOLS=[ "vcbuildtool", "boost" ]
# This is for the built in SCons Microsoft Visual Studio Support
PROJECT_TOOLS = [ "msvc", "mslink", "boost" ]
VC_BUILD_TOOLS_PATH="c:/Program Files (x86)/Microsoft Visual C++ Build Tools"
BOOST_INCLUDE_PATH="D:/Dev/libraries/boost_1_62_0"
BOOST_LIB_PATH="D:/Dev/libraries/boost_1_62_0/stage/lib"
BOOST_LIBRARIES="none"
CINDER_INCLUDE_PATH="C:/wsr/local/libraries/cinder/include"
CINDER_LIB_PATH="C:/wsr/local/libraries/cinder/lib/msw/x86"
CINDER_LIB="cinder-v140"
PROJECT_CXXFLAGS=["/EHsc"]
