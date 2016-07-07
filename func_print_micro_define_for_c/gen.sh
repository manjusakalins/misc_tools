cat $1 | grep "#define" > 1
echo a | awk '{printf("{\n\tswitch(cmd) {\n")}' > out
cat 1 | awk '{print $2}' | awk '{printf("\tcase %s:\n\t{\n\t\tprintk(\"###############%s\\n\");\n\t\tbreak;\n\t}\n", $0,$0)}' >> out
echo abc | awk '{printf("\tdefault:\n\t\tprintk(\"default micro:%s \\n\", cmd);break;\n", "%x")}' >> out
echo a | awk '{printf("\t}\n}\n");}' >> out
