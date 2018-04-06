# SCons Tempalate #

This is meant to be a simple and flexible framework for working with SCons.

Environment variables are defined under ./site_scons/xscons.py 

Tools (definitions that help comiple specific libraries go under ./site_scons/site_tools). To add support for a new library, add it here.

User-specific options (library locations, compiler paths) are specified in ./options_<platofm>.py in the same directory as the SConstruct.

This is should be a good layout for small projects, keeping as much per-library and per-platform logic out of the main SConstruct as possile.

Right now this uses Visual Studio Build Tools on Windows, rather than Visual Studio itself.