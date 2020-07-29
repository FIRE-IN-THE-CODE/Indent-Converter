# Indent Converter
Indent Converter is a small scripted program intended to fix the indentation of Python scripts from tabs to
four spaces in accordance to the PEP 8 Code Styling guide.

Note: As an extra precaution for data loss, it is recommended that you backup any of the scripts this program
will be used on.

## Requirements
Requires Python3 to be installed.

### Build Status
In progress.

### How to Use
Indent Converter uses a command line interface. The syntax is:
tab_converter.py <command> [option - file name]

-f   --file          select the script to convert
-h   --help          prints usage information
-m   --mix           mixes the indents into tabs and spaces
-o   --output        gives the name to the new converted file
-r   --repair        fixes the script to make all indents into 4 spaces


