#!/usr/bin/python3

import string
import time
import os
import subprocess

## TODO:
# Fix the static asset copying.
# Make a multi-page generator.

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
	# Generate the Table of Contents
	toc = generate_toc(sections)
	# Combine the TOC and Sections to form the Content.
	content = generate_content(toc, sections)
	# Get the timestamp.
	timestamp = generate_timestamp()
	# Get the first 7 of git commit SHA
	commit_id = generate_commit_id()
	# Titles are hardcoded for now, change this when we add multipage support.
	title = "Cuberite User's Manual"
	head_title = title
	# Write the actual content.
	with open(os.path.join(output_directory, "index.html"), "w") as f:
		f.write(template.safe_substitute(content=content,
		timestamp=timestamp,
		title=title,
		head_title=head_title,
		commit_id=commit_id))
	# Copy the static stuff to the out directory.
	os.system("cp -r " + input_directory + "/static/* " + output_directory + "/")

def load_template():
	with open(os.path.join(input_directory, "template.html"), "r") as template_file:
		# Read all of the data from the file and return it.
		return string.Template(template_file.read())

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
	for s in os.listdir(os.path.join(input_directory, "book_ko")):
		# We only want directories, not any other files hanging around in the
		# book subfolder.
		if not os.path.isdir(os.path.join(input_directory, "book_ko", s)):
			continue
		# Add the section to the dictionary.
		sections[s] = {}
		# Run through all of the subsections in that section and load them.
		for ss in os.listdir(os.path.join(input_directory, "book_ko", s)):
			# If we're not looking at a file, ignore it.
			if not os.path.isfile(os.path.join(input_directory, "book_ko", s, ss)):
				continue
			# Load the subsection and insert it into the sections dict.
			with open(os.path.join(input_directory, "book_ko", s, ss), "r") as ss_file:
				sections[s][os.path.splitext(ss)[0]] = ss_file.read()
	# Return the generated sections.
	return sections

def split_section(section):
	return section.split(" - ", 1)

def generate_link(section):
	if single_page:
		return "".join(
			["<a href=\"#", split_section(section)[0], "\">", split_section(section)[1], "</a>"]
		)
	else:
		return "".join(
			["<a href=\"", split_section(section)[0], ".html\">", split_section(section)[1], "</a>"]
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
	toc = ["<div id=\"toc\">"]
	for s in sorted(sections):
		# Add the Section Header.
		toc.append("<a href=\"#" + split_section(s)[0] + "\" class=\"section-header\">"  + s + "</a>")
		toc.append("<ul>")
		# Now the subsections.
		for ss in sorted(sections[s]):
			toc.append("<li>" + generate_link(split_section(split_section(s)[0] + "." + ss)[0] + " - " + split_section(s)[0] + "." + ss) + "</li>")
		toc += ["</ul>"]
	toc.append("</div>")
	return "\n".join(toc)

def generate_content(toc, sections):
	if single_page:
		content = []
		content.append(toc)
		content.append("<div id=\"manual-content\">")
		for s in sorted(sections):
			content.append("<section>")
			content.append("<h2 id=\"" + split_section(s)[0] + "\">"  + s + "</h2>")
			for ss in sorted(sections[s]):
				content.append("<section>")
				content.append("<h3 id=\"" + split_section(s)[0] + "." + split_section(ss)[0] + "\">" + ss + "</h3>")
				content.append(sections[s][ss])
				content.append("</section>")
			content.append("</section>")
		content.append("</div>")
		return "\n".join(content)

def generate_timestamp():
	date = time.strptime(subprocess.check_output(['git', 'log', '-1', '--format=%cd']).strip().decode(),
	"%a %b %d %H:%M:%S %Y %z")
	return time.strftime("%d %B %Y", date)

def generate_commit_id():
	return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).strip().decode()

# Run the main function.
main()
