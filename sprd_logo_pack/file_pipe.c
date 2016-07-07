#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>


#if defined(MSDOS) || defined(OS2) || defined(WIN32) || defined(__CYGWIN__)
#  include <fcntl.h>
#  include <io.h>
#  define SET_BINARY_MODE(file) setmode(fileno(file), O_BINARY)
#else
#  define SET_BINARY_MODE(file)
#endif

#define CHUNK 16384

//size_t fread ( void *buffer, size_t size, size_t count, FILE *stream) ;
//size_t fwrite(const void* buffer, size_t size, size_t count, FILE* stream);
int dump(FILE *source, FILE *dest)
{
    int rsize=0;
    int wsize=0;
   	unsigned char in[CHUNK];
	unsigned char out[CHUNK];
	fseek (source, 0, SEEK_END);
	int in_size = ftell(source);
	fseek (source, 0, SEEK_SET);

    printf("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ %s %d to dump: %d##########\n", __func__, __LINE__, in_size);
    while(in_size > 0) {
        rsize = fread(in, 1, CHUNK, source);
        wsize = fwrite(in, 1, rsize, dest);
        if (rsize != wsize) {
            printf("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ %s %d ##########\n", __func__, __LINE__);
            return -1;
        }
        in_size -= rsize;
    }
    /*
    wsize = fwrite(out, 1, rsize, dest);
    if (rsize != wsize) {
        printf("########## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ %s %d ##########\n", __func__, __LINE__);
        return -1;
    }*/
    return 0;
}

// structre of pinfo:
// pinfo[0] ==> num of chunk 
// pinfo[1] ==> size of whole out file
// pinfo[2] ==> offset of zip chunk[1]
// pinfo[3] ==> offset of zip chunk[2]
// ...
// pinfo[n+1] ==> offset of zip chunk[n]
// "offset" is the distance from the begining of the file, not the zip chunk
#define IN_FILE_OFFSET (3)
int main(int argc, char **argv)
{
	int ret = 0;
	int i;
	FILE *input, *output;
    printf("input argc: %d\n", argc);
	if (argc < 3 || (strcmp(argv[1], "-p") && strcmp(argv[1], "-d"))) 
	{
		printf("[Usage] compress -p output input1 [input2]\n");
		printf("Example: compress -p out.raw input1.raw input2.raw\n");
		return -1;
	}

	// compress
	if(!strcmp(argv[1], "-p"))
	{
		char *ptemp;
		unsigned int *pinfo;

		int filenum = argc - 1;
		printf("input argc: %d, read: %s, write %s, file num:%d\n", argc, argv[IN_FILE_OFFSET], argv[IN_FILE_OFFSET-1], filenum);

		input = fopen(argv[IN_FILE_OFFSET], "rb");
		output = fopen(argv[IN_FILE_OFFSET-1], "wb");
        printf("########## %s %d ##########%p %p\n", __func__, __LINE__, input, output);
		ptemp = (char*)malloc(1024*1024);
		pinfo = (unsigned int*)malloc(filenum*sizeof(int));
		if(input < 0 || output < 0 || ptemp == NULL || pinfo == NULL || input == NULL || output == NULL)
		{
			fprintf(stderr, "open file and allocate temp buffer fail\n");
			fprintf(stderr, "input = %p, output = %p, ptemp = 0x%p, pinfo = 0x%p\n", input, output, ptemp, pinfo);
			ret = -1;
			goto done;
		}
        //printf("########## %s %d ##########\n", __func__, __LINE__);

		memset((void*)pinfo, 0, sizeof(int)*filenum);
		// write information header to output first
		if(sizeof(int)*filenum != fwrite(pinfo, 1, filenum*sizeof(int), output))
		{
			ret = -2;
			goto done;
		}

        //firt chunk start offset.
		pinfo[pinfo[0]+2]=ftell(output);
		if (dump(input, output)) 
		{
			ret = -2;
			goto done;
		}
		pinfo[0] = pinfo[0]+1;

		for (i = IN_FILE_OFFSET+1; i < argc; i++) 
		{
			fclose(input);

			input = fopen(argv[i], "rb");
            printf("########## %s %d ########## open %s\n", __func__, __LINE__, argv[i]);
			pinfo[pinfo[0]+2]=ftell(output);
			if (dump(input, output)) 
			{
				fprintf(stderr, "compress error\n");
				ret = -2;
				goto done;
			}
			pinfo[0] = pinfo[0]+1;
		}
        printf("########## %s %d ########## done\n", __func__, __LINE__);
done:
		fseek(output, 0L, SEEK_END);
		pinfo[1] = ftell(output);
		fseek(output, 0L, SEEK_SET);
		fwrite(pinfo, 1, filenum*sizeof(int), output);

        if (input != NULL) fclose(input);
		fclose(output);
		free(ptemp);
		free(pinfo);

		return ret;
	}
#if 0 //skip dedump files
	// decompress
	else
	{
		unsigned int temp;
		unsigned int *pinfo;
		char outputfilename[256];
		input = fopen(argv[3], "rb");
		if(input < 0)
		{
			printf("open file fail\n");
			printf("input = %d\n", input);
			ret = -1;
			goto done2;
		}

		fread(&temp, 1, sizeof(int), input);
		printf("temp=%d\n", temp);
		pinfo = malloc(temp*sizeof(int));
		if(pinfo == NULL)
		{
			printf("allocate pinfo failed\n");
			ret = -1;
			goto done2;
		}

		fread(pinfo, 1, temp*sizeof(int), input);

		for(i=0;i<temp;i++)
			printf("pinfo[%d]=%d\n", i, pinfo[i]);

		for(i = 0;i < temp;i++)
		{
			sprintf(outputfilename, "%d_%s", i, argv[2]);
			output = fopen(outputfilename, "wb");
			if(output < 0)
			{
				printf("create output file %s fail\n", outputfilename);
				goto done2;
			}

			fseek(input, pinfo[i], SEEK_SET);
			if(Z_OK != inf(input, output))
			{
				printf("decompress error\n");
				ret = -2;
				goto done2;
			}

			fclose(output);
			output = 0;
		}
done2:
		fclose(input);
		if(output) fclose(output);
		return ret;

	}
#endif
	return 0;

}
