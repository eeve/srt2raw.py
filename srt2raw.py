#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Convert subtitle file (utf-8) to raw text.'

__author__ = 'eeve'

version = 'v1.0.0'

import os
import sys
import re

reg = r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3})\s{1}-->\s{1}(\d{2}:\d{2}:\d{2},\d{3})\n'

argvCount = len(sys.argv)

if argvCount == 2 and (sys.argv[1] == '-V' or sys.argv[1] == '--version'):
	print(version)
	exit()

# output help information
if argvCount == 1 or (argvCount == 2 and (sys.argv[1] == '-h' or sys.argv[1] == '--help')):
	print('''
Usage: srt2raw.py [options]

Options:

	-h, --help           output usage information
	-V, --version        output the version number
	-f, --file <path>    *set srt file path
	-o, --output <path>  set output file path
	-l, --linenumber     show line number
	-t, --timeline       show timeline
	-e, --extname <extname>  set output file extname

Examples:

	$ srt2raw.py -f /path/to/file.srt -o /path/to/dist/filename -l -t
	$ srt2raw.py -f /path/to/file.srt -l -t
	''')
else:

	try:
		fileIndex = sys.argv.index('-f')
		filePath = os.path.abspath(sys.argv[fileIndex + 1])
	except:
		print('ERROR: Re-run using the -h to output usage information！')
		exit()

	try:
		extNameIndex = sys.argv.index('-e')
		extName = sys.argv[extNameIndex + 1]
	except:
		extName = '.txt'

	try:
		outputIndex = sys.argv.index('-o')
		outputPath = sys.argv[outputIndex + 1]
	except:
		outputPath = filePath
	finally:
		outputPath = os.path.abspath(outputPath)
		outputPath = os.path.join(os.path.dirname(outputPath), os.path.splitext(os.path.basename(outputPath))[0] + extName)
		print('Use the default output path: %s' % outputPath)

	try:
		lineNumber = sys.argv.index('-l')
		lineNumber = True
	except:
		lineNumber = False

	try:
		timeLine = sys.argv.index('-t')
		timeLine = True
	except:
		timeLine = False

	try:
		f = open(filePath, 'r', encoding="utf-8")
		content = f.read()
		arr = re.split(reg, content)
	except Exception as e:
		print('ERROR: The srt file path is incorrect!')
		print(e)
		exit()

	lines, tempStr = [], None

	for i in list(filter(lambda i: (i - 1) % 4 == 0, range(1, len(arr)))):
		tempStr = ""
		index = arr[i]
		startTime = arr[i+1]
		endTime = arr[i+2]
		word = arr[i+3]

		# 加上字幕序号
		if lineNumber:
			tempStr += index + '.';

		# 加上时间轴
		if timeLine:
			tempStr += ' '+ startTime + ' - ' + endTime + ' ';

		# 加上字幕
		tempStr += word
		lines.append(tempStr)

	try:
		w = open(outputPath, 'w', encoding="utf-8")
		w.write(''.join(lines))
		w.close()
		print('Total %d records. writing succeeded!' % len(lines))
	except:
		print('ERROR: File writing failed！')
