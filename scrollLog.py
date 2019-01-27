

def scroll_text(log, scroll_position, max_lines):
    max_index = max_lines if max_lines < len(log) else len(log)
    max_index += scroll_position
    display_array = log[scroll_position:max_index]
    text: str = ""
    for i in range(len(display_array)):
        text += display_array[i]
        if (i != len(display_array) - 1):
            text += "\n"
    return text