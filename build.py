from pybuilder.core import use_plugin, init
import os

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('pypi:pybuilder_aws_plugin')

name = "rds_log_dog"
default_task = "publish"
version = "0.1"

@init
def set_properties(project):
    project.set_property('bucket_prefix', 'dist/')
    project.version = '%s.%s' % (project.version, os.environ.get('BUILD_NUMBER', 0))
