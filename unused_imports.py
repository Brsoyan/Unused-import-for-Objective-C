# This code for python 3

import os, glob, re
from collections import Counter

# your project path
project_path = "/Users/user/Desktop/your-Project"
files = [];
# you can set file prefix which you need to find
prefix = "SC"

#if you need to remove unused categories imports chanage this BOOL
remove_categories = False

# If in your project you have classes which #imports you doesn't need to remove.
# Or classes for static object
# Like this static NSString *CELL_IDENTIFIER = @"mainCell"; ....
# And does not need to delete import add the classes names in constant_classes list.

constant_classes = ["HBConstantString", "HBApiCallUrls"] # ....


def find_files_recursive(path):
	for filename in os.listdir(path):
		if os.path.isdir(path + "/" + filename):
			find_files_recursive(path + "/" + filename)

		for filename in glob.glob(os.path.join(path, '*.m')):
			# Finde file with prefix
			words = filename.split("/")
			last_Word = words[-1]
			if len(prefix) > 0:
				if last_Word.startswith(prefix) and filename not in files:
					files.append(filename)
			elif filename not in files:
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
				if constant_classes.count(word) > 0 and word not in class_names:
					class_names.append(word)
					f.write(line)
				elif word.startswith(prefix) or word.startswith("NS"):
					if not remove_categories:
						if "+" in word and word not in class_names:
							class_names.append(word)
							f.write(line)
						else:
							count = 0
							for x_word in lines:
								if x_word.count(word) > 0:
									count += 1
							if word not in class_names and count != 1:
								class_names.append(word)
								f.write(line)
					else:
						count = 0
						for x_word in lines:
							if x_word.count(word) > 0:
								count += 1

						if word not in class_names and count != 1:
							class_names.append(word)
							f.write(line)
				else:
					f.write(line)
			else:
				f.write(line)
		f.close()
		
print("Finish")

