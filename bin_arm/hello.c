#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char** argv) {

   printf("hello world\n");
	FILE *filp;
	filp = fopen(KMSG_FILE, "r");
    int ret=0;
   char buffer[2048];
   memset(buffer, 0, 2048);
   FILE *fversion;
   fversion = fopen("/proc/version", "r");
   if (fversion == NULL){
       printf("open file error\n");
       return -1;
   }
    ret=fread(buffer, 1, 2048, fversion);
    if (ret <=0)
        printf("error\n");
    printf("%s:%d\n", buffer, ret);
    printf("%s\n", strstr(buffer, "SMP PREEMPT"));
    char *strs = strstr(buffer, "SxMP PREEMPT");
    if (strs == NULL)
        printf("fdfdfd");
   return 0;
}