#first object is the target


#curltest:$(OBJ_FILE)
#	g++ $^ -o $@


CC=g++
include_dirs=-I/usr/local/include
CFLAGS=$(include_dirs)
#LIBS=-L/usr/local/lib -lcurl -lm -lpthread


EXECUTABLE=curltest
SRCS=$(wildcard *.cpp)
all:
	$(CC) $(CFLAGS) $(SRCS) $(LIBS)-o $(EXECUTABLE)

#JSON_OBJ=json.o wrap_json.o test_json.o
#OBJ_XQ=xq.o xq_curl.o psocket.o xq_other.o
#rxq:$(JSON_OBJ) $(OBJ_XQ)
#	$(CC) $(CFLAGS) -o $@ $^ $(LIBS)

#all:$(rxq)

clean:
	@echo "clean project"  
	-rm *.o
	@echo "clean complete

