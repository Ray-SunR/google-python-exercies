#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib2

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def purify(list):
  ret = []
  for item in list:
    if item not in ret:
      ret.append(item)
  return ret


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  hostname = filename[filename.find('_') + 1:]
  with open(filename, 'r') as file:
    contents = file.read()
    pattern = r'\S*.jpg'
    pattern1 = r'(\S*-\w*-(\w*).jpg)'
    ret = re.findall(pattern, contents)
    ret1 = re.findall(pattern1, contents)
    ret1.sort(key=lambda tuple: tuple[1])
    ret1list = [tuple[0] for tuple in ret1]
    
    ret1purify = purify(ret1list)
    retpurify = purify(ret)

    ret1purify = ['http://' + hostname + item for item in ret1purify]
    retpurify = ['http://' + hostname + item for item in retpurify]

    retpurify.sort()
    file.close()
    return ret1purify
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  htmldata = '<html>\n<body>\n'
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
  idx = 0
  for url in img_urls:
    print('Retrieving: ' + url)
    sys.stdout.flush()
    handle = urllib2.urlopen(url)
    header = handle.info()
    if handle.getcode() != 200:
      print('Error retrieving link: ' + url)
      print('Quiting program!')
      sys.exit(-1)

    imgdata = handle.read()
    imgpath = os.path.join(dest_dir, 'img' + str(idx) + '.jpg')
    with open(imgpath, 'w') as imgfile:
      imgfile.write(imgdata)
      imgfile.close()
      imghtml = '<img src="' + 'img' + str(idx) + '.jpg' + '">\n'
      htmldata += imghtml
      idx += 1
  htmlfile = open(os.path.join(dest_dir, 'index.html'), 'w')
  htmldata += '</body>\n</html>\n'
  htmlfile.write(htmldata)


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
