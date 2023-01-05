#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert a new node into  a sorted list
 * @head: head of list
 * @number: new number
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL); }
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new); }
	if (number < (*head)->n)
	{
		new->next = *head;
		return (new); }
	else if (current->n > number)
	{
		new->next = current; }
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > number)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			else
			{
				current = current->next; }}
		current->next = new; }
	return (new);
}
