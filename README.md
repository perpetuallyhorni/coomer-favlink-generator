# Coomer Favlink Generator

## What is Coomer Favlink Generator (CFG)?
It is a command-line tool that outputs regular links to a .txt file from the JSON file you receive when you parse the [Coomer API](https://coomer.su/api/schema) for your favorites. 
It's designed to streamline the process of getting all your coomer.su favorites as links in order to batch download them with [Cyberdrop-DL](https://github.com/Jules-WinnfieldX/CyberDropDownloader).

## Why?
If you have lots of favorites on coomer.su, getting the list of links manually can take a while... CFG automates this task, saving you time and effort.

## When to use it?
After you have parsed your favorites from the coomer.su API and have the resulting JSON file.

## Installation
The only officially supported method of installation is through [pipx](https://github.com/pypa/pipx), which allows you to install Python CLI tools in isolated environments and execute them from any directory in your system. This ensures that CFG does not interfere with your system's Python packages.
Alternatively, you can download the source code and use conda, create a venv or whatever alternate method you want but I will not provide support for installations not made with pipx.

To install CFG, make sure you have pipx installed and run the following command:

`
pipx install coomer_favlink_generator
`

NOTE: While CFG should work on Windows, it is not officially supported (I don't have a Windows machine), thus no guarantees are made regarding its functionality on that platform. However, contributions in the form of pull requests and issues are welcome.


## How to Use It
Ensure you have the JSON file named with the prefix `response_` in your current directory.
Open a terminal and run:
`
coomer_favlink_generator
`

NOTE: If there are multiple files with this prefix or none at all, the tool will prompt you to provide the location of the desired file.

The output will be a text file named `coomer_links.txt` in your current directory, containing all the generated links.

## Disclaimer
CFG is not affiliated with, authorized by, endorsed by, or in any way connected with Coomer, Kemono, OnlyFans, Fansly, CandFans or any of their subsidiaries or affiliates.

## License
Coomer Favlink Generator is open-sourced software licensed under the MIT license. See the LICENSE file for more details.
