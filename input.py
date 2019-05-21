
# Things needed by magic.py:
# 1. Functions:
#     1. get_page_contents
# 2. variables:
#     1. user_interval (int - time (seconds) between checks)
#     2. user_tolerance (int - max number of acceptable differences)
#     3. user_end_after_success (boolean - stop process after a change has been found)
#     4. One of the following (have these as options for user to choose from - output ones not chosen as 0):
#       a. user_max_checks (int - max checks before stopping)
#       b. user_duration (int - time (minutes) before stopping process)
#       c. user_infinite (boolean - go forever, no limit to time or checks)
# Things needed by output.py:
# 1. Variables:
#     1. twilio_num
#     2. user_num
#     3. account_sid
#     4. auth_token
#     5. user_interval
#     6. user_end_after_success
#     7. user_max_checks
