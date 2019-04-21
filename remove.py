#!/usr/bin/env python3
# remove.py version 1.0
# Copyright (C) 2019 Dakota Walsh

import os  # file operations
import sys # system operations

def main():
	# public web directory with the images
	web_dir = "/var/www/html/" # EDIT THIS FOR YOUR SERVER
	max_disk_percent = 0.00 # Max disk usage percentage out of 1

	# determine the current disk usage
	stat  = os.statvfs(web_dir)
	total = stat.f_blocks*stat.f_bsize
	free  = stat.f_bfree*stat.f_bsize
	used  = 1-(free/total)
	# if it's less than the max disk percent exit
	if (used < max_disk_percent):
		sys.exit(0)

	# get a list of all the files
	file_list = os.listdir(web_dir)
	print(file_list)

if __name__ == '__main__':
	main()
