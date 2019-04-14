
import os
import shutil
from pipemap.pipes import parse_slide_pipes
from pipemap.html_utils import get_bare_html_page, get_link_str

def get_bare_css():
    """
    generate empty css page to populate
    """
    bare_css = ""
    return bare_css

def merge_slide_style(css_str, style_dict):
    """
    grow an existing css string with new rules inside a style_dict
    """
    print("TODO: css merging")
    return css_str

def parse_markdown(tile_md):
    """
    parse markdown string, return corresponding html
    """
    print("TODO: markdown parsing")
    tile_lines_list = [
            "<p>" + line + "</p>"
            for line in tile_md.splitlines()]
    tile_str = os.linesep.join(tile_lines_list)
    return tile_str

def generate_index_slide(
        index_str,
        prev_link=None,
        next_link=None):
    """
    generate string for the html index slide
    """
    return generate_slide(
            index_str,
            prev_link=prev_link,
            next_link=next_link)

def generate_slide(
        slide_str,
        prev_link=None,
        next_link=None):
    """
    generate string for a standard slide
    """
    tiles_list = parse_slide_pipes(slide_str)
    html_prefix, html_suffix = get_bare_html_page()
    slide_style_dict = {}
    slide_html = ""
    for tile in tiles_list:
        slide_html += parse_markdown(tile)
    if prev_link is not None:
        slide_html += os.linesep + get_link_str(prev_link, "previous slide")
    if next_link is not None:
        slide_html += os.linesep + get_link_str(next_link, "next slide")
    slide_html = html_prefix + slide_html + html_suffix
    return slide_html, slide_style_dict

def generate_slide_names(
        nb_slides):
    slide_names = [
        "slide_%03d"%(i_s)
        for i_s in range(nb_slides)]
    return slide_names

def populate_pres_folder(
        dest_folderpath,
        index_slide_html,
        slides_html_list,
        pres_css,
        slide_names,
        dont_create_new_folder=False,
        warn_if_dest_not_empty=False,
        ):
    if not os.path.exists(dest_folderpath):
        if not os.path.exists(os.path.dirname(dest_folderpath)):
            raise IOError("""Cannot create pres folder, parent path does not
                    exist (%s)."""%(os.path.dirname(dest_folderpath)))
        if dont_create_new_folder:
            raise IOError("""Pres destination folder path does not exist (%s),
                    requested not to create one."""%(dest_folderpath))
        os.mkdir(dest_folderpath)
    if os.listdir(dest_folderpath):
        if warn_if_dest_not_empty:
            raise IOError("""destination folder is not empty (%s), but requested
                    not to erase."""%(dest_folderpath))
        shutil.rmtree(dest_folderpath)
        os.mkdir(dest_folderpath)

    with open(os.path.join(dest_folderpath,"index.html"), "w") as index_file:
        index_file.write(index_slide_html)

    nb_slides = len(slides_html_list)
    for i_s in range(nb_slides):
        with open(
                os.path.join(dest_folderpath, "%s.html"%(slide_names[i_s])),
                "w") as slide_file:
            slide_file.write(slides_html_list[i_s])
    with open(
            os.path.join(dest_folderpath,"pres.css"),
            "w") as slide_file:
        slide_file.write(pres_css)


