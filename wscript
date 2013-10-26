#!/usr/bin/env python
# encoding: utf-8

from waflib.Tools import waf_unit_test

APPNAME='test_travis'
VERSION='0.1'

top='.'
out='build'

def options(opt):
  opt.load('compiler_cxx boost waf_unit_test')
  try:
      opt.load('xcode')
  except ImportError:
      pass

def configure(conf):
  #conf.env['CXX'] = 'clang++'
  conf.load('compiler_cxx boost waf_unit_test')

  cc_version = conf.env['CC_VERSION']
  if (cc_version[0] <= '4' and cc_version[1] <= '6'):
      c11_flag = '-std=c++0x'
  else:
      c11_flag = '-std=c++11'
  if (conf.env['CXX'][0].endswith('/g++')):
      conf.env.append_value('CXXFLAGS', [c11_flag, '-g'])

  elif (conf.env['CXX'][0] == 'clang++'):
      conf.env.append_value('CXXFLAGS', [c11_flag, '-g', '-stdlib=libc++'])
      conf.env.append_value('LINKFLAGS', [c11_flag, '-stdlib=libc++'])

  root_env=conf.env

  # release conf
  conf.setenv('release', env=root_env.derive())
  # test conf
  conf.setenv('test', env=root_env.derive())
  conf.check_cc(lib='gcov', define_name='HAVE_GCOV', mandatory=False)
  if (conf.env['CXX'][0].endswith('/g++')):
      # should be only for tests
      if (conf.is_defined('HAVE_GCOV')):
          conf.env.append_value('CXXFLAGS', ['--coverage', '-fprofile-arcs', '-ftest-coverage'])
          conf.env.append_value('LDFLAGS',['--coverage'])

  # recurse into source directory
  conf.recurse('src')

def build(bld):
  # accept only variants
  if (not bld.variant):
    #bld.fatal('call "waf test" or "waf release", and try "waf --help"')
    return
  bld.recurse('src')


# add test context used with "build test" command
from waflib.Build import BuildContext
class test(BuildContext):
    cmd = 'test'
    variant = 'test'

class release(BuildContext):
    cmd = 'release'
    variant = 'release'
