x = "jknv qwdklb alkwjef aljfln sdfnklsjnal aglwkgn asdfkjbadjhbjw ads alkjsfba ad kljabfk afhbawblkf afhblsbdaflkjk awlkjfbklwabfkjln awfkljbwablk"
y = "jknv qwdulb alkwjef aljfln sdfnklsjnal aglwkgm asdfkjbadjhbjw ads alkjsfba ad kljabfk afhbawbokf afiblsbdajlkjk awlkjfbklwabfkjln awfoojbwablk"
x_segment = x[50:100]
y_segment = y[50:100]
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

count = sum(1 for a, b in zip(x_segment, y_segment) if a != b)
print(count)