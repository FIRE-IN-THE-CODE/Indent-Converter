# Indent Converter
Indent Converter is a small scripted program intended to fix the indentation of Python scripts from tabs to
four spaces in accordance to the PEP 8 Code Styling guide.

<b>Note:</b> As an extra precaution for an unintended script edit, it is recommended that you backup any of the scripts 
this program will be used on.

<b>This is a pre-release and is not ready for use.</b>

## Requirements
Requires Python3 to be installed.

## How to Use
Indent Converter uses a command line interface. The syntax is: <br>
tab_converter.py &#60;command&#62; [option]
<pre>
-f   --file          select the script to convert
-h   --help          prints usage information
-m   --mix           mixes the indents into tabs and spaces
-o   --output        gives the name to the new converted file
-r   --repair        fixes the script to make all indents into 4 spaces
</pre>

