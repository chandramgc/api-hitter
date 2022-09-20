#   -*- coding: utf-8 -*-
from ensurepip import version
from re import U
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("exec")


name = "pybuilder-demo"
version = "1.0"
default_task = ["clean","install_dependencies","publish","package"]


@init
def set_properties(project):
    # Build Dependencies
    project.build_depends_on("pyinstaller")    
    project.build_depends_on("mockito")
    # Dependencies
    project.depends_on("selenium")

