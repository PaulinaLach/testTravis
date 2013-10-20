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
  # FIXME: use gcov only for tests
  conf.check_cc(lib='gcov', define_name='HAVE_GCOV', mandatory=False)

  cc_version = conf.env['CC_VERSION']
  if (cc_version[0] <= '4' and cc_version[1] <= '6'):
      c11_flag = '-std=c++0x'
  else:
      c11_flag = '-std=c++11'
  if (conf.env['CXX'][0].endswith('/g++')):
      conf.env.append_value('CXXFLAGS', [c11_flag, '-g'])
      # should be only for tests
      if (conf.is_defined('HAVE_GCOV')):
          conf.env.append_value('CXXFLAGS', ['--coverage', '-fprofile-arcs', '-ftest-coverage'])
          conf.env.append_value('LDFLAGS',['--coverage'])
  elif (conf.env['CXX'][0] == 'clang++'):
      conf.env.append_value('CXXFLAGS', [c11_flag, '-g', '-stdlib=libc++'])
      conf.env.append_value('LINKFLAGS', [c11_flag, '-stdlib=libc++'])
  conf.check_boost(lib='program_options unit_test_framework', mt=True, static=False)

def build(bld):
  bld.recurse('src')
