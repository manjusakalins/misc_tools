cat $1 | grep "#define" > 1
cat 1 | awk '{print $2}' | awk '{printf("case %s:\n{\n\tprintk(\"###############%s\\n\");\n\tbreak;\n}\n", $0,$0)}' > out
echo abc | awk '{printf("default:\n\tprintk(\"default micro:%s \\n\", cmd);break;\n", "%x")}' >> out
