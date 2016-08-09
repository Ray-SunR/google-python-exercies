#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
  ret = []
  files = os.listdir(dir)
  pattern = r'__\w+__'
  for file in files:
    if re.search(pattern, file):
      ret.append(os.path.abspath(os.path.join(dir, file)))
  return ret


def copy_to(paths, to_dir):
  for path in paths:
    file_names = os.listdir(path)
    print(file_names)
    abs_fps = [os.path.join(path, file) for file in file_names]
    for abs_path in abs_fps: 
      if os.path.isfile(abs_path):
        if not os.path.exists(to_dir):
          os.makedirs(os.path.join(to_dir))
        print('Copying %s to %s' % (abs_path, to_dir))
        shutil.copy2(abs_path, to_dir)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  print(args)
  if args[0] == '--todir':
    copy_to(args[1], args[2])
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  else:
    print(get_special_paths(args[0]))

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
