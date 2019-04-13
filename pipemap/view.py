
import shutil

def generate_index_slide(
        index_str):
    """
    generate string for the html index slide
    """
    import ipdb; ipdb.set_trace()
    index_slide_html = ""
    index_slide_css = ""
    return index_slide_html, index_slide_css

def generate_slide(
        slide_str):
    """
    generate string for a standard slide
    """
    slide_html = ""
    slide_css = ""
    return slide_html, slide_css

def populate_pres_folder(
        dest_folderpath,
        index_slide_htmlcss,
        slides_htmlcss_list,
        dont_create_new_folder=False,
        warn_if_dest_not_empty=False,
        ):
    if not os.path.exist(dest_folderpath):
        if not os.path.exist(os.path.dirname(dest_folderpath)):
            raise IOError("""Cannot create pres folder, parent path does not
                    exist (%s)."""%(os.path.dirname(dest_folderpath)))
        if dont_create_new_folder:
            raise IOError("""Pres destination folder path does not exist (%s),
                    requested not to create one."""%(dest_folderpath))
        os.path.makedir(dest_folderpath)
    if os.listdir(dest_folderpath):
        if warn_if_dest_not_empty:
            raise IOError("""destination folder is not empty (%s), but requested
                    not to erase."""%(dest_folderpath))
        shutil.rmtree(dest_folderpath)
        os.path.makedir(dest_folderpath)

    with open(os.path.join(dest_folderpath,"index.html"), "w") as index_file:
        index_file.write(index_slide_html[0])
    with open(os.path.join(dest_folderpath,"index.css"), "w") as index_file:
        index_file.write(index_slide_html[1])

    nb_slides = len(slides_html_list)
    for i_s in range(nb_slides):
        with open(
                os.path.join(dest_folderpath,"slide_%03d.html"%(i_s)),
                "w") as slide_file:
            slide_file.write(slides_html_list[i_s][0])
        with open(
                os.path.join(dest_folderpath,"slide_%03d.css"%(i_s)),
                "w") as slide_file:
            slide_file.write(slides_html_list[i_s][1])


