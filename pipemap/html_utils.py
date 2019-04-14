
import os

def get_bare_html_page():
    """
    generate empty html page to populate
    """
    bare_html_prefix = os.linesep.join([
        "<!DOCTYPE html>", "<html>", "<body>"])
    bare_html_suffix = os.linesep.join([
        "</body>", "</html>"])
    return bare_html_prefix, bare_html_suffix

def get_link_str(
        tgt_page_name,
        link_name):
    """
    get string corresponding to an html link
    """
    return "<a href=\"%s.html\">%s</a>"%(tgt_page_name, link_name)

def get_numbering_str(
        numbering):
    """
    get string corresponding to an html link
    """
    return "<p>%d</p>"%(numbering)

