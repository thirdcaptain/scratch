#include "struct_header.h"

int main (int argc, int **argv)
{
	char *buffer = NULL;
	size_t bufsize = 0;
	int num_chars = 0, i = 0;

	while(1)
	{
		i = 0;
		printf("$$$ ");
		num_chars = getline(&buffer, &bufsize, stdin);
		while (buffer[i] != '\0')
		{
			if (buffer[i + 1] == '\0')
				buffer[i] = '\0';
			i++;
		}
		printf("character count: %d\n", num_chars);
		printf("%s\n", buffer);
	}
	return(EXIT_SUCCESS);
}
