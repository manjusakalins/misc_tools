#first please rewrite xls to do gen for vbat_q.h
python do_gen.py > vbat_q.h
gcc -o run run.c
./run

