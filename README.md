# Jiddo_Legacy

This project demonstrates web scraping techniques to extract article titles, links, and paragraphs from a website. The code is implemented in Python and uses various modules and libraries for web scraping.

## TODO-list

- [x] Store information to a file
- [ ] BUG: Parsed information of script doing wickidy weird things
- [ ] Dates that the article was posted from the site
- [ ] BONUS: Copy of the articles WRITTEN version (from his actual writing, and even the old ones to add it)
- [ ] BONUS: Translation to the articles for English (then expand to other languages if popularity takes in)
- [ ] BONUS: React w/ Python?

## Story

This project is dedicated to my grandfather, Dr. Zaid Hamzeh. He writes passionately about the problems we are surrounded in the world, and how blinded we can be in our own bubble. His courage and thinking has been touched to me and dearing to understand myself and others, both of which are strengths and reinforcements of our weaknessess.

As I admire him much and he someone I love and adore, I wanted to keep up his work and save it somewhere in the future and share it with others who are into the _lore_.

## Features

- Modify non-ascii URL to satisfies link content of the site
- Parses multiple `<div>`, `<a href>`, `<p>`, and regular HTML text to extrapolate necessary information as needed
- Extracted data will be a console output, and it can be further manipulated if needed

## Prerequisite

- Python 3.x

## Requirements

- pip3

## Usage

**Note**: This assumes that you have `virtualenv` installed.
Useful notes: If you see some text with `<...>` in it, means you can add whatever it is required to fill in.

- Open your terminal
- git clone https://github.com/zedin27/Jiddo_Legacy `<name_of_folder>`
- cd `<name_of_folder>`
- `./run.sh`
- `python3 webscrapping.py`
