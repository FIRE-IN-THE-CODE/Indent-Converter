<h1 align='center'>Indent Converter</h1>

![Build](https://img.shields.io/badge/Build_Status-Complete-green)
![Python](https://img.shields.io/badge/Python-3-blue)

Indent Converter is a small scripted program created to reformat the indentation of other Python scripts converting tabs into
four spaces to follow the PEP 8 style guide or mix tabs and four space indents to mess with someone's Python project.


## Requirements
Requires Python3 to be installed.


## Usage Information
Indent Converter uses a command line interface. <br>
Syntax format: &#60;command&#62; [file name] [option]

<pre>
Commands:
-h   --help          prints usage information
-m   --mix           mixes  tabs and four spaces for every indent
-r   --repair        reformat the script converting every tab into four spaces

Optional:
-o   --output        sets the argument as the name for the new file
</pre>
