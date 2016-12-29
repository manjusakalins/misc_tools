#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char** argv) {

#if 0
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
#endif
   	FILE *filp;
    float data[3];
    data[0] = 0.1;
    data[1] = 0.2;
    data[2] = -0.1;

	filp = fopen("common_acc.bin", "w+");
	fwrite(data, 1, sizeof(data), filp);
	fclose(filp);
   return 0;
}
