
import sys
import os

import click

from .pipes import parse_pres_pipes, parse_slide_pipes
from .view import generate_index_slide,generate_slide, populate_pres_folder

@click.group()
def cli():
    pass

@cli.command()
@click.argument('pres_desc_filepath', nargs=1)
@click.argument('dest_folderpath', nargs=1)
@click.option('--dont_create_new_folder', default=False)
@click.option('--warn_if_dest_not_empty', default=False)
def compile_pres(
        pres_desc_filepath,
        dest_folderpath,
        dont_create_new_folder=False,
        warn_if_dest_not_empty=False,
            ):
    """
    Compile an html-based presentation from a presentation description file.
    The corresponding presentation will be generated inside the designated
    folder.
    """
    with open(pres_desc_filepath, 'r') as pres_desc_file:
        pres_desc_str = pres_desc_file.read()

    # parse pres structure
    index_str, slides_str_list = parse_pres_pipes(
            pres_desc_str)

    # parse tiles
    index_slide_htmlcss = generate_index_slide(index_str)
    slides_htlmcss_list = [
            generate_slide(slide_str)
            for slide_str in slides_str_list]

    # generate HTML & CSS
    populate_pres_folder(
            dest_folderpath,
            index_slide_htmlcss,
            slides_htlmcss_list,
            dont_create_new_folder,
            warn_if_dest_not_empty,
            )

if __name__ == "__main__":
    cli()

