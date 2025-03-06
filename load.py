"""
Start of MeritTracker, a tool to show how many merits you have.
Because of the way the journal system works, the merit count is
only updated at the start of a session. This can therefore be used
to track how many merits you earn in a session based on how many are displayed
by the plugin and how many are displayed in the game. Note that this will
not keep track of merits earned in specific systems, so it is best to keep
Powerplay activity to one system if you want to best use this plugin.
"""
from __future__ import annotations

import logging
import tkinter as tk
from config import appname

from typing import Optional, Tuple
import l10n
import functools
_ = functools.partial(l10n.Translations.translate, context=__file__)

# This **MUST** match the name of the folder the plugin is in.
PLUGIN_NAME = "merittracker"

logger = logging.getLogger(f"{appname}.{PLUGIN_NAME}")

merits: Optional[tk.label]


class MeritTracker:

    def __init__(self) -> None:
        logger.info("MeritTracker instantiated")

    def on_load(self) -> str:
        return PLUGIN_NAME

    def setup_main_ui(self, parent: tk.Frame) -> Tuple[tk.Label, tk.Label]:
        global merits
        label = tk.Label(parent, text="Merits:")
        merits = tk.Label(parent, text="")
        return label, merits

    def journal_entry(self, event: str, state: Dict[str, Any]) -> None:
        global merits
        if event == 'Powerplay':
            logger.info('Deteted Powerplay event')
            merits["text"] = state['Powerplay']['Merits']


mt = MeritTracker()

def plugin_start3(plugin_dir: str) -> str:
    return mt.on_load()


def plugin_stop() -> None:
    logger.info('Stopping MeritTracker')


def plugin_app(parent: tk.Frame) -> tk.Label | None:
    return mt.setup_main_ui(parent)

def journal_entry(cmdrname: str, is_beta: bool, system: str, station: str, entry: dict, state: dict) -> None:
    """
    Update Merit count any time we get a Powerplay event
    """
    mt.journal_entry(entry['event'], state)
    

