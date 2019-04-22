#!/usr/bin/env python3
# remove.py version 1.0
# Copyright (C) 2019 Dakota Walsh

import os  # file operations
import sys # system operations

def sorted_ls(path):
	# sort the web_dir by age
	mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
	return list(sorted(os.listdir(path), key=mtime))

def main():
	# public web directory with the images
	web_dir = "/var/www/html/" # EDIT THIS FOR YOUR SERVER
	max_disk_percent = 0.80 # Max disk usage percentage out of 1

	# determine the current disk usage
	stat  = os.statvfs(web_dir)
	total = stat.f_blocks*stat.f_bsize
	free  = stat.f_bfree*stat.f_bsize
	used  = 1-(free/total)
	# if it's more than the max disk percent remove oldest file
	while (used > max_disk_percent):
		os.remove(os.path.join(web_dir, sorted_ls(web_dir)[0]))
		stat  = os.statvfs(web_dir)
		total = stat.f_blocks*stat.f_bsize
		free  = stat.f_bfree*stat.f_bsize
		used  = 1-(free/total)

if __name__ == '__main__':
	main()
