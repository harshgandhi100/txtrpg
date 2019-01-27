

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

def translate(value, from_min, from_max, to_min, to_max):
    # Figure out how 'wide' each range is
    leftSpan = from_max - from_min
    rightSpan = to_max - to_min

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - from_min) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return to_min + (valueScaled * rightSpan)

def get_scroll_bar_details(log, scroll_position, max_lines):
    # default x-value = 1000
    # y value range 130, 380
    x_value = 1000
    y_start = translate(scroll_position, 0, len(log), 130, 380)
    y_end = translate(scroll_position + max_lines, 0, len(log), 130, 380)
    return ((x_value, y_start), (x_value, y_end))