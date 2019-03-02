# emailtemplates

Title: Emails & Templates
Version: 1.0
Created By: Shawn Fogarty
Purpose: Simple script that internally stores commonly used templates that can be retrieved by entering a short keyword that will copy the template to your clipboard for easy pasting into any application. The templates are hard coded into the script and geared towards usage in a Technical Support environment.

Setup / Usage Instructions:
1. Install Python interpreter from: https://www.python.org/downloads/
2. Install add-on pyperclip from cmd prompt using: pip install pyperclip.
3. Unzip the otemails file to same location Python is installed.
4. Edit templates.bat file to specify the path where you unzipped the templates.py file.
5. Add the path where Python and the script files are located to Windows Environment variable System > PATH section.
6. Press Win+R to open the run box.
7. Enter: templates <template lookup keyword>
8. Press enter and the template you choose will be copied to clipboard.
9. Open application where you want template to go and press CTRL+V (or right click / paste).

Template lookup arguments keywords and their description:
initial = Initial email to customer stating the issue.
pie = Problem, Impact, Expected Behavior summary.
1stfu = First follow-up email.
2ndfu = Second follow-up email.
survey = Request to provide survey response.

Usage example:
Entering the following on the run box: "templates initial" results in the initial follow-up template being copied to the clipboard. 

Note: It's possible to convert this script to an exe using pyinstaller and modifying the bat file
