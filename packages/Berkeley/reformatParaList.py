import sys
import json


def reformatParaList(text, num_arg):
    argstring1 = ""
    argstring2 = ""
    for i in range(num_arg):
        argstring1 += "#"+str(i+1)
        if i+1 < num_arg:
            argstring2 += "#"+str(i+1) + ","
        else:
            argstring2 += "#"+str(i+1)

    return r"\def\{0}{1}{{\gdef\@{0}{{{2}}}}}".format(text, argstring1, argstring2) + "\n"


filename = sys.argv[1]

json_input = open(filename+".json", "r")
json_input_loaded = json.load(json_input)
json_output = open(filename+".txt", "w")
for line in json_input_loaded:
    json_output.write(reformatParaList(line, json_input_loaded[line]))
json_input.close()
json_output.close()
