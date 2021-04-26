#! /usr/bin/env python3

import sys
import re

#first i'm just going to put the code to see if I can understand it better without docstrings on my screen

def find_iter(in_stream, target_regex,
        start_regex = None,
        stop_regex = None):

    search_has_started = False
    if not start_regex:
        search_has_started = True
    for line_index, line in enumerate(in_stream):
        if stop_regex and stop_regex.match(line):
            break
        if start_regex and (not search_has_started):
            if start_regex.match(line):
                search_has_started = True
            continue
        for match_object in target_regex.finditer(line):
            yield line_index, match_object

def record_all_occurrences(in_stream, out_stream,
        target_regex,
        start_regex = None,
        stop_regex = None):
