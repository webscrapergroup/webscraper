
from input import text_new, text_old, get_page_contents
count = sum(1 for a, b in zip(text_old, text_new) if a != b)
