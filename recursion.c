#include <stdio.h>

int count(int num)
{
	if (num <= 10)
	{
		printf("%d\n", num);
		return(count(num + 1));
	}
	return(num);
}

int main (void)
{
	int final_num;
	final_num = count(1);
	printf("\nfinal_num: %d\n", final_num);
	return(0);
}
