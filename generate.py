#!/usr/bin/python3

import string
import codecs
import os

## TODO:
# Copy static assets (perhaps copy into file iteslf) function.
# Generate Table of Contents Function
# Writing to outfolder function.
# Generate headings with ids to be linked to.

# Temporary global variables for the input and output directories.
input_directory = "."
output_directory = "out"

# Global Configuration Variable - do we use single page or multi?
single_page = True

def main():
	# First off, load all of the data from disk into memory.
	template = load_template()
	sections = load_sections()
	# Run through the sections and linkify.
	for s in sections:
		for ss in sections[s]:
			sections[s][ss] = linkify(sections[s][ss])
	print(sections)

def load_template():
	with codecs.open(
		os.path.join(input_directory, "template.html"),
		"r", encoding="UTF-8"
	) as template_file:
		# Read all of the data from the file and return it.
		return template_file.read()

def load_sections():
	# First, define an empty dictionary to contain the section data.
	# This dictionary will consist of keys of section names, with values of 
	# dictionaries with keys of subsection names and values containing 
	# subsection data. An example:
	#
	# dict = {
	#     "0 - Introduction": {
	#         "1 - Intro1": "<p>This is Intro1</p>",
	#         "2 - Intro2": "<p><b>This is BOLD Intro2</b></p>"
	#     }
	# }
	sections = {}
	# Now we go through all of the section directories.
	for f in os.listdir(os.path.join(input_directory, "book")):
		# We only want directories, not any other files hanging around in the
		# book subfolder.
		if not os.path.isdir(os.path.join(input_directory, "book", f)):
			continue
		# Add the section to the dictionary.
		sections[f] = {}
		# Run through all of the subsections in that section and load them.
		for ss in os.listdir(os.path.join(input_directory, "book", f)):
			# If we're not looking at a file, ignore it.
			if not os.path.isfile(os.path.join(input_directory, "book", f, ss)):
				continue
			# Load the subsection and insert it into the sections dict.
			with codecs.open(
				os.path.join(input_directory, "book", f, ss),
				"r", encoding="UTF-8"
			) as ss_file:
				sections[f][ss_file] = ss_file.read()
	# Return the generated sections.
	return sections

def split_section(section):
	return section.split(" - ", 1)

def generate_link(section):
	if single_page:
		return "".join(
			["<a href=\"#", split_section(section)[0], "\">", section, "</a>"]
		)
	else:
		return "".join(
			["<a href=\"", split_section(section)[0], ".html\">", section, "</a>"]
		)

def linkify(text):
	# First, loop over the text.
	while len(text.split("{{", 1)) == 2:
		st = text.split("{{", 1)
		sst = st[1].split("}}", 1)
		sst[0] = generate_link(sst[0])
		text = st[0] + sst[0] + sst[1]
	return text

# Run the main function.
main()
