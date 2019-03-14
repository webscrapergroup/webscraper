
x = "jknv qwdklb alkwjef aljfln sdfnklsjnal aglwkgn asdfkjbadzhbjw ads alkjsfba aq kljabfk afhbawblkf afhblsbdaflkjk awlkjfbklwabfkjln awfkljbw"
y = "jknv qwdulb alkwjef aljfln sdfnklsjnal mglwkgm asdfkjtadjhbjw ads alkjsfba ad kljabmk afhbawbokf afiblsbdajlnjk nwlkjfbklwabfkjln awfoojbw"
x_segment = x[50:100]
y_segment = y[50:100]
# print(x)
# print(len(x)) #142
# print(x_segment)
# print(len(x_segment)) #50
# print(len(x_segment))

# from difflib import Differ
# import re
# # for (i, j) in (x_segment, y_segment):
# #     print(i)
# def find_line_diff(str1, str2):
#     # Initialize the Differ class as d
#     d = Differ()

#     # Create a list of the differences found by the compare method
#     result = list(d.compare(str1, str2))
#     return(result)
#     # print(result)

# differences = find_line_diff(x_segment, y_segment)
# print(str(differences))
# # regex_test = re.findall("^+$", differences)
# # print(regex_test)

# Magical - use this for everything
count = sum(1 for a, b in zip(x_segment, y_segment) if a != b)
print(str(count) + " changes")