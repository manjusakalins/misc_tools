#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <fcntl.h>
#include <time.h>

#define KERNEL_VERSION_FILE ("/proc/version")
int main(int argc, char **argv)
{
    char buf[1024] = {0};
    int rlen=0;
    int fd=0;
    fd = open(KERNEL_VERSION_FILE, O_RDONLY);
     if (fd <= 0) {
        printf("Open fail, return\n");
        return -1;
    }
    
    rlen = read(fd, buf, 1024);
    if (rlen <= 0 || rlen == 1024) {
        printf("read failed : %d\n", rlen);
        close(fd);
        return -1;
    }
    char *start = strstr(buf, "SMP");
    printf("%s\n", start); //SMP XXXX
    close(fd);
    
    struct tm time;
    strptime(start, "SMP %a %b %d %H:%M:%S UTC %Y", &time);
    printf("%d %d %d %d\n", time.tm_year, time.tm_mon, time.tm_mday);
    time_t loctime = mktime(&time);  // timestamp in current timezone
    time_t gmttime = timegm(&time);  // timestamp in GMT
    printf("%lld\n", (long long)loctime);
    printf("%lld\n", (long long)gmttime);
    return 0;
    
}
