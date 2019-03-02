#! python3
# templates.py - A program to quickly copy common email/note templates to windows clipboard for quick pasting anywhere.

EMAILS = {'1stfu': 'Hello , Since I have not heard back from you I would like to follow-up on the status of this \n'
                   'ticket.',
          '2ndfu': 'Hello , I am following up on this ticket as I have not yet received a response from you. \n'
                   'I will keep the ticket open for 2 business days and then I will close it if I do not hear back \n'
                   'from you. If you do need to revisit this later simply open a new ticket and reference this \n'
                   'ticket so we can easily continue. Thanks.',
          'initial': 'Hello ,\n'
                     'I am looking forward to assisting you and I would like to ask that you confirm if the following\n'
                     ' statement of your issue/request is correct:\n'
                     '<insert PS>',
          'pie':   'Problem Statement: Content Server - \n'
                   'Expected Behavior: \n'
                   'Impact: \n'
                   '\n'
                   'Environment:\n'
                   '\n'
                   '1st occurance: \n'
                   'Last known change: '
                   '\n'
                   'Steps to reproduce:\n'
                   '\n'
                   'Scope (what is/is not affected):\n'
                   'WHAT\n'
                   '\n'
                   'WHERE \n'
                   '\n'
                   'WHEN \n'
                   '\n'
                   'EXTENT \n'
                   '\n'
                   'Current Troubleshooting Steps\n'
                   '\n'
                   'Possible Cause(s):\n'
                   '\n'
                   'True Cause / Resolution:',
          'survey': 'If you have any feedback to share about my service please take a moment to fill out the upcoming\n' 
                    ' survey, thanks!'
          }

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python templates.py [EMAILS] - enter template keyword to auto copy to clipboard.')
    sys.exit()

template = sys.argv[1] # first cmd line argument is the lookup keyword (ex: 1stfu)

if template in EMAILS:
    pyperclip.copy(EMAILS[template])
    print('Email for ' + template + ' copied to clipboard.')
else:
    print('There is no Email Template for ' + template)
