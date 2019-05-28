import time
from input import get_page_contents, user_interval, user_max_checks, user_tolerance, user_end_after_success, user_duration, user_forever, url
from output import found_change, time_checked, date_checked, change_detected, 

#send text while this var is true
send_text = False
#internal var for num of checks made
check_count = 0

#checks for one of three conditions
while ((check_count < user_max_checks) or ((user_interval*check_count/60) < user_duration)) or (user_forever == True):
    #reset differences
    differences_count = 0
    #get page contents
    contents_old = get_page_contents()
    #wait
    time.sleep(user_interval)
    #get contents
    contents_new = get_page_contents()
    #update check count
    check_count += 1
    #check differences between slices of page contents strings
    differences_count = sum(1 for a, b in zip(contents_old, contents_new) if a != b)
    #check if the differences are greater than what the user specifies
    if(differences_count >= user_tolerance or (abs(len(contents_old)) - len(contents_new)) > user_tolerance):
        send_text = True
        found_changes ()
        if(user_end_after_success == True):
            break
        else:
            continue
    else:
        continue
