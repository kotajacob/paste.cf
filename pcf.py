#!/usr/bin/env python3
# pcf.py version 1.0
# Copyright (C) 2019 Dakota Walsh

import os         # file operations
import sys        # system operations
import ftplib     # ftp operations
import argparse   # argument parsing
import hashlib    # calculate hash

def getHash(f_name):
	# return a hash of the file in question with the extension
	root = ''
	ext	 = ''
	# however first we'll get the extension if there is one
	if '.' in f_name:
		root, ext = os.path.splitext(f_name)
	# calculate the hash of the file
	f_hash = hashlib.sha1(open(f_name,'rb').read()).hexdigest()
	return(f_hash + ext)

def checkFile(upload_file, max_file):
	# check that the directories exist
	if not (os.path.isfile(upload_file)):
		print ("ERROR: File not found! Check your spelling and ensure the file exists.")
		sys.exit(1)
	if not (os.path.getsize(upload_file) <= (max_file)):
		print ("ERROR: File too large. If this is a mistake, edit pcf.py to change max_file.")
		sys.exit(1)

def getArgs():
	# get the arguments with argparse
	arg = argparse.ArgumentParser(description="pcf.py")
	arg.add_argument('file', metavar='F', help='The file which should be uploaded.')
	return arg.parse_args()

def main():
	# get the passed arguments
	arguments    = getArgs()
	upload_file  = arguments.file
	server_addr  = "paste.cf" # the server's address
	server_pub   = "incoming" # public subdirectory on the server
	max_file     = 10*1024*1024 # error if the file is over this size

	# check that the file exists and is less than max_file
	checkFile(upload_file, max_file)

	# login to paste.cf and change into the public directory
	ftp = ftplib.FTP(server_addr, "anonymous", "pcfclient")
	ftp.cwd(server_pub)

	# upload the file then close the connection
	ftp.storbinary("STOR " + upload_file, open(upload_file, 'rb'))
	ftp.quit()

	# calculate the sha1sum and print the url
	new_url = "https://" + server_addr + "/" + getHash(upload_file)
	print(new_url)

if __name__ == '__main__':
	main()
