#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>

int main(void)
{
	char *file_input = "/home/manjusaka/pre13.bin";
	char *file_output = "/home/manjusaka/all_codes/my_codes/read_bin/text";
	char data[2048];
	char str[256];

	int ret;
	int file_in, file_out;
	file_in = open(file_input, O_RDONLY);
	if (file_in <= 0 ) {
		printf("file open error %s %d\n", __func__, __LINE__);
		return -1;
	}

	file_out = open(file_output, O_RDWR|O_CREAT|O_TRUNC,0777);
	if (file_out <= 0 ) {
		printf("file open error %s %d\n", __func__, __LINE__);
		ret = file_out;
		goto open_error;
	}
	
	ret = read(file_in, data, 2048);
	if (ret!=2048) {
		printf("read file error %s %d: %d\n", __func__, __LINE__, ret);
		goto out;
	}
	/*
	str = (char *)mmap(0, 8*2048,PROT_READ|PROT_WRITE, MAP_SHARED|MAP_ANONYMOUS, file_out, 0);
	if (str == MAP_FAILED)
    {
        perror("mmap");
        return -1;
    }
	*str=0;
	printf("read file error %s %d: %d 0x%x\n", __func__, __LINE__, ret, (unsigned int)str);
	*/
	int i=0;
	for(; i < 2048; i++) {
		if (i%16 == 0)
			write(file_out, "\n", 1);
		sprintf(str, "0x%02x, ", data[i]&0xff);
		write(file_out, str, strlen(str));
	}
	
out:
	close(file_out);
open_error:
	close(file_in);

}
