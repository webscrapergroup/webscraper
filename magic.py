import time
from input import get_page_contents, user_interval, user_max_checks, user_tolerance, user_end_after_success
# count = sum(1 for a, b in zip(text_old, text_new) if a != b)

send_text = False
check_count = 0
while True:
    contents_old = get_page_contents()
    time.sleep(user_interval)
    contents_new = get_page_contents()
    differences_count = sum(1 for a, b in zip(contents_old, contents_new) if a != b)
    if(differences_count >= user_tolerance):
        send_text = True
        if(check_count >= user_max_checks or user_end_after_success == True):
            break
        else:
            continue
    else:
        if(check_count >= user_max_checks):
            break
        else:
            continue
