
import sys
import os

import click

from pipemap.pipes import parse_pres_pipes, parse_slide_pipes
from pipemap.view import generate_index_slide,generate_slide, populate_pres_folder, get_bare_css, merge_slide_style, generate_slide_names

@click.group()
def cli():
    pass


# Some general presentation properties
# They probably ultimately need tom move to a user-modifyable config file
def read_config_file(
        config_filepath=""
        ):
    if config_filepath != "":
        raise NotImplementedYet("")
    config_dict = {
            "pres_css_name": "pres",
            }
    return config_dict


@cli.command()
@click.argument('pres_desc_filepath', nargs=1)
@click.argument('dest_folderpath', nargs=1)
@click.option('--config_filepath', default="")
@click.option('--dont_create_new_folder', default=False)
@click.option('--warn_if_dest_not_empty', default=False)
def compile_pres(
        pres_desc_filepath,
        dest_folderpath,
        config_filepath="",
        dont_create_new_folder=False,
        warn_if_dest_not_empty=False,
            ):
    """
    Compile an html-based presentation from a presentation description file.
    The corresponding presentation will be generated inside the designated
    folder.
    """
    config_dict = read_config_file(config_filepath)


    with open(pres_desc_filepath, 'r') as pres_desc_file:
        pres_desc_str = pres_desc_file.read()

    # parse pres structure
    index_str, slides_str_list = parse_pres_pipes(
            pres_desc_str)
    nb_slides = len(slides_str_list)
    index_name = "index"
    slide_names = generate_slide_names(nb_slides)

    # parse tiles
    index_slide_html, index_slide_style = \
            generate_index_slide(
                    index_str,
                    prev_link=None,
                    next_link=slide_names[0] if nb_slides>0 else None)
    slides_html_list = []
    slides_style_list = []
    pres_css = get_bare_css()
    pres_css = merge_slide_style(pres_css, index_slide_style)
    for i_s, slide_str in enumerate(slides_str_list):
        slide_html, slide_style = \
            generate_slide(
                slide_str,
                prev_link=slide_names[i_s-1] if i_s>0 else index_name,
                next_link=slide_names[i_s+1] if i_s<(nb_slides-1) else None,
                numbering=i_s,
                css_filename=config_dict["pres_css_name"],
                )

        pres_css = merge_slide_style(pres_css, slide_style)
        slides_html_list.append(slide_html)

    # generate HTML & CSS
    populate_pres_folder(
            dest_folderpath,
            index_slide_html,
            slides_html_list,
            pres_css,
            slide_names,
            dont_create_new_folder,
            warn_if_dest_not_empty,
            pres_css_name=config_dict["pres_css_name"],
            )

if __name__ == "__main__":
    cli()

