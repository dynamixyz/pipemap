
import os
import shutil
from pipemap.pipes import parse_slide_pipes

def get_bare_page():
    """
    generate empty html+css page to populate
    """
    bare_html_prefix = os.linesep.join([
        "<!DOCTYPE html>", "<html>", "<body>"])
    bare_html_suffix = os.linesep.join([
        "</body>", "</html>"])
    bare_css = ""
    return bare_html_prefix, bare_html_suffix, bare_css

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
        index_str):
    """
    generate string for the html index slide
    """
    return generate_slide(index_str)

def generate_slide(
        slide_str):
    """
    generate string for a standard slide
    """
    tiles_list = parse_slide_pipes(slide_str)
    html_prefix, html_suffix, slide_css = get_bare_page()
    slide_html = ""
    for tile in tiles_list:
        slide_html += parse_markdown(tile)
    slide_html = html_prefix + slide_html + html_suffix
    return slide_html, slide_css

def populate_pres_folder(
        dest_folderpath,
        index_slide_htmlcss,
        slides_htmlcss_list,
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
        index_file.write(index_slide_htmlcss[0])
    with open(os.path.join(dest_folderpath,"index.css"), "w") as index_file:
        index_file.write(index_slide_htmlcss[1])

    nb_slides = len(slides_htmlcss_list)
    for i_s in range(nb_slides):
        with open(
                os.path.join(dest_folderpath,"slide_%03d.html"%(i_s)),
                "w") as slide_file:
            slide_file.write(slides_htmlcss_list[i_s][0])
        with open(
                os.path.join(dest_folderpath,"slide_%03d.css"%(i_s)),
                "w") as slide_file:
            slide_file.write(slides_htmlcss_list[i_s][1])


