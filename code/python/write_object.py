# -*- coding: utf-8 -*-

import array
import collections
import glob
import hashlib
import numpy
import os
import sys
import re
import tempfile

import ROOT

def write_object(root_file, root_object, path):
		root_file.cd()
		root_directory = root_file
		for directory in path.split("/")[:-1]:
			if root_directory.Get(directory) == None:
				root_directory.mkdir(directory)
			root_directory = root_directory.Get(directory)
			root_directory.cd()
		root_object.Write(path.split("/")[-1], ROOT.TObject.kWriteDelete)
		root_file.cd()
