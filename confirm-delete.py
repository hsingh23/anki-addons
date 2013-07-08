# -*- coding: utf-8 -*-
# © 2013: Roland Sieker <ospalh@gmail.com>
#
# License: GNU GPL, version 3 or later;
# http://www.gnu.org/copyleft/gpl.html
#


u"""
Anki 2 add-on to ask before deleting notes.
"""

from anki.hooks import wrap
from aqt.reviewer import Reviewer
from aqt.browser import Browser
from aqt.utils import askUser

__version__ = "0.0.1"


def browser_ask_delete(browser, _old=None):
    u"""Ask whether we should delete notes from the browser."""
    if not browser.selectedNotes():
        # Re-do bits from the original function. No need to ask if we
        # should delete 0 notes.
        return
    if askUser('Delete selected notes?', defaultno=True):
        # Always asks before deleting notes here.
        _old(browser)


def reviewer_ask_delete(reviewer, _old=None):
    u"""Ask whether we should delete notes during reviews."""
    if reviewer.mw.state != "review" or not reviewer.card:
        # Re-do bits here, too. Delete only in review mode.
        return
    if askUser('Delete note?', defaultno=True):
        # Always asks before deleting notes here.
        _old(reviewer)

Browser.deleteNotes = wrap(Browser.deleteNotes, browser_ask_delete, 'wrap')

## If you have the colorful_toolbars add-on installed and get TWO
## delete questions during reviews, delete the line below.
Reviewer.onDelete = wrap(Reviewer.onDelete, reviewer_ask_delete, 'wrap')
