#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - is palindorme?
 * @head: input linked list
 * Return: 1(palindrome) or 0 (not palindrome)
 */

int is_palindrome(listint_t **head)
{
	const listint_t *current;
	unsigned int n; /* number of nodes*/
	int *elements;
	int cur_elem;
	unsigned int index;

	current = *head;
	n = 0;
	/* find n */
	while (current !=  NULL)
	{
		current = current->next;
		n++; }
	if (n == 0)
	{
		return (1); }
	elements = malloc(sizeof(int) * n);
	if (elements == NULL)
	{
		return (1); }
	n = 0;
	current = *head;
	while (current != NULL)
	{
		cur_elem = current->n;
		current = current->next;
		n  = n + 1;
		elements[n] = cur_elem; }
	index = 1;
	while (index < n / 2)
	{
		if (elements[index] != elements[n - index + 1])
		{
			return (0); }
		index++; }
	free(elements);
	return (1);
}
