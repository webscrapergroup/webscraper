import time
from input import get_page_contents, user_interval, user_max_checks, user_tolerance, user_end_after_success, user_duration

send_text = False
check_count = 0

while (check_count < user_max_checks) and ((user_interval*check_count/60) < user_duration):
    contents_old = get_page_contents()
    time.sleep(user_interval)
    contents_new = get_page_contents()
    check_count += 1
    differences_count = sum(1 for a, b in zip(contents_old, contents_new) if a != b)
    if(differences_count >= user_tolerance):
        send_text = True
        if(user_end_after_success == True):
            break
        else:
            continue
    else:
        continue