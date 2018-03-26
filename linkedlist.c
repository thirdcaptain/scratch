#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct list_s
{
	int index;
	char *string;
	struct list_s *next;

} list_t;

/**
 * makes a linked list with index and string, then asks user to change value based on index
 *
 */

int main (int argc, char **argv)
{
	list_t *head = NULL;
	list_t *middle = NULL;
	list_t *end = NULL;
	list_t *cursor = NULL;
	int num;

	head = malloc(sizeof(list_t));
	if (head == NULL)
		return (1);
	middle = malloc(sizeof(list_t));
	if (middle == NULL)
		return (1);
	end = malloc(sizeof(list_t));
	if (end == NULL)
		return (1);

	/*check for proper number of arguments*/
	if (argc != 3)
	{
		printf("Usage is %s with two arguments\n", argv[0]);
		free(end);
		free(middle);
		free(head);
		return(-1);
	}

	num = atoi(argv[1]);
	if (num > 2 || num < 0)
	{
		printf("Index must be between 0 - 2\n");
		free(end);
		free(middle);
		free(head);
		return(-1);
	}

	/*prints arguments*/
	printf("argv[0]: %s, argv[1]: %s, argv[2]: %s\n", argv[0], argv[1], argv[2]);

	/*initialize head*/
	head->index = 0;
	head->string = "HEAD";
	head->next = middle;

	/*initialize middle*/
	middle->index = 1;
	middle->string = "MIDDLE";
	middle->next = end;

	/*initialize end*/
	end->index = 2;
	end->string = "END";
	end->next = NULL;

	/*print list - BEFORE*/
	cursor = head;
	printf("list elements BEFORE change\n");
	while (cursor != NULL)
	{
		printf("index: %d\n", cursor->index);
		printf("string: %s\n", cursor->string);
		cursor = cursor->next;
	}

	/*traverses through linked list to index*/
	cursor = head;
	while (cursor->index != num)
	{
		cursor = cursor->next;
	}
	/*changes string value to new string value*/
	cursor->string = strdup(argv[2]);

	/*print list - AFTER*/
	printf("list elements AFTER change\n");
	cursor = head;
	while (cursor != NULL)
	{
		printf("index: %d\n", cursor->index);
		printf("string: %s\n", cursor->string);
		cursor = cursor->next;
	}

	free(end);
	free(middle);
	free(head);

	return(0);
}
