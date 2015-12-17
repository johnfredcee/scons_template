# Copyright (C) 2015 John Connors.
#
# This program is free software: you can redistribute it and/or  modify
# it under the terms of the GNU Affero General Public License, version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import platform
from SCons.Defaults import *
import xscons


optfile = "options_"+platform.system().lower()+".py"
print "Looking for options in ", optfile
vars = Variables(optfile)
env = xscons.make_root_env(vars);
env.Program("hello_boost", [ "hello_boost.cpp" ])
