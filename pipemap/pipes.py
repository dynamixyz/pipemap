
#def _get_first_char_ind(line_str):
#    """
#    get first non-space character of a line
#    """
#    i_c = 0
#    first_char_ind = -1
#    while line_str[i_c] == " "  and i_c < len(line_str):
#        i_c += 1
#    if i_c < len(line_str):
#        first_char_ind = i_c
#    return first_char


def parse_pres_pipes(pres_desc_str):
    """
    Parse presentation structure.
    This function separates the code of the different slides of the
    presentation.
    """
    slide_tokens = pres_desc_str.split("--")

    if len(slide_tokens) < 2:
        print("""No complete slide found (to be complete, a slide must be
                surrounded by double-pipes '--').""")
        return "", []

    index_str = slide_tokens[1]
    slides_str_list = slide_tokens[2:]

    return index_str, slides_str_list

def parse_slide_pipes(slide_desc_str):
    """
    Parse slide content.
    This function parses the content of a slides, constructs the visual
    representation.
    """
    tile_tokens = slide_desc_str.split("-")
    return tile_tokens





