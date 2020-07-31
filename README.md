<h1 align='center'>Indent Converter</h1>

![Build](https://img.shields.io/badge/Build_Status-In_Progress-red)
![Python](https://img.shields.io/badge/Python-3-blue)

Indent Converter is a small scripted program intended to fix the indentation of other Python scripts by converting tabs to
four spaces in accordance to the PEP 8 guide.

## Requirements
Requires Python3 to be installed.

## How to Use
Indent Converter uses a command line interface. The syntax is: <br>
tab_converter.py &#60;command&#62; [file name] [option]
<pre>
-h   --help          prints usage information
-m   --mix           mixes the indents into tabs and spaces
-o   --output        gives the name to the new converted file
-r   --repair        fixes the script to make all indents into 4 spaces
</pre>

