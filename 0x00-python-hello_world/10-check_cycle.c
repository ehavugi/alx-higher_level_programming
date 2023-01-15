#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check if list contain a cycle
 * @list: head of a list
 * Return: 0 if no cycle, 1 if there a cycle
 */
int check_cycle(listint_t *list)
{
	int size  = 0;
	listint_t *head = list;
	listint_t *ptr  = list;
	int MAX = 100000; /* A number of possibly larger list*/

	if (list == NULL)
	{
		return (0);
	}

	while (head->next != NULL)
	{
		size += 1;
		head = head->next;
		if (head == ptr)
		{
			return (1);
		}
		if (size > MAX)
		{
			return (1);
		}
	}
	return (0);
}
