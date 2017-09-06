# This code for python 3

import os, glob, mmap, re, fileinput


# your project path
project_path = "/Users/user/Desktop/project_PATH"
files = [];
# you can set file prefix which you need to find
prefix = "HB"

def find_files_recursive(path):
	for filename in os.listdir(path):
		if os.path.isdir(path + "/" + filename):
			find_files_recursive(path + "/" + filename)

		for filename in glob.glob(os.path.join(path, '*.m')):
			# Finde file with prefix
			words = filename.split("/")
			last_Word = words[-1]
			if len(prefix) > 0:
				if last_Word.startswith(prefix):
					files.append(filename)
			else:
				files.append(filename)

find_files_recursive(project_path)

for file in files:
	class_names = []
	if len(files) > 0:
		f = open(file,"r")
		lines = f.readlines()
		f.close()

		f = open(file,"w")
		for line in lines:
			if line.startswith("#import"):
				words = line.split()
				word = re.sub('["]', '', words[1].split(".")[0])
				if word not in class_names:
					class_names.append(word)
					f.write(line)
			else:
				f.write(line)

		f.close()

	print(class_names)






