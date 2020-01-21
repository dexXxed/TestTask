# use the sample.json file.
# This file contains JSON that has a list of objects inside.
# Open the file in a code editor,
# try to identify some pattern on it and check it's structure first. Each object is under unique ID:
#
# {
#
#     "SV350": {... // data, describing the object...},
#
#     "fKDFI3": {... // data, describing the object...},
#
#     ...
#
#     "38shF": {... // data, describing the object...}
#
# }
#
# Therefore, you need to write one regular expression to extract the following information:
# Every unique ID on this file ( for example, the first unique ID should be NC065 and the last should be NN574).
# Hint: The length of your list should be 211
import re


# WRITE YOUR REGULAR EXPRESSION HERE
Regexp_JSON = r'(?<=")[a-zA-Z0-9]{5}(?=":{)'
with open(r'sample.json', "r") as f:
    json = f.read()

print('----- Expressions extracted -----')
print("First unique id: {}".format(re.findall(Regexp_JSON, json)[0]))
print("Last unique id: {}".format(re.findall(Regexp_JSON, json)[-1]))
print("Length of list of unique ids: {}".format(len(re.findall(Regexp_JSON, json))))
