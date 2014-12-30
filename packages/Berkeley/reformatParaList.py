import sys
import json
import os


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
json_output1 = open(filename+".txt", "w")
json_output2 = open(filename+".sty", "w")
json_output2.write(
    r"\ProvidesPackage{packages/" +
    os.path.basename(os.getcwd()) +
    r"/filename}" + "\n\n"
    )
for line in json_input_loaded:
    json_output1.write(reformatParaList(line, json_input_loaded[line]))
    json_output2.write(reformatParaList(line, json_input_loaded[line]))
json_input.close()
json_output1.close()
json_output2.close()
