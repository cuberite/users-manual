#!/usr/bin/python3

import string
import os

## TODO:
# Copy static assets (perhaps copy into file iteslf) function.
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
	# Generate the Table of Contents
	toc = generate_toc(sections)
	print(toc)

def load_template():
	with open(os.path.join(input_directory, "template.html"), "r") as template_file:
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
	for s in os.listdir(os.path.join(input_directory, "book")):
		# We only want directories, not any other files hanging around in the
		# book subfolder.
		if not os.path.isdir(os.path.join(input_directory, "book", s)):
			continue
		# Add the section to the dictionary.
		sections[s] = {}
		# Run through all of the subsections in that section and load them.
		for ss in os.listdir(os.path.join(input_directory, "book", s)):
			# If we're not looking at a file, ignore it.
			if not os.path.isfile(os.path.join(input_directory, "book", s, ss)):
				continue
			# Load the subsection and insert it into the sections dict.
			with open(os.path.join(input_directory, "book", s, ss), "r") as ss_file:
				sections[s][ss] = ss_file.read()
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

def generate_toc(sections):
	toc = ["<h1 id=\"toc\">Table of Contents</h1>", "<ul>"]
	for s in sections:
		# Add the Section Header.
		toc += ["<li>", s, "<ul>"]
		# Now the subsections.
		for ss in sections[s]:
			toc.append("<li>" + generate_link(ss) + "</li>")
		toc += ["</ul></li>"]
	toc.append("</ul>")
	return "\n".join(toc)

# Run the main function.
main()
