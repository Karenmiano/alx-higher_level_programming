#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a new node in a sorted singly linked list
 * @head: pointer to pointer to head of singly linked list
 * @number: number to be stored in new node
 * Return: address of new node if insertion is successful, NULL if otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *trav;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL || (*head)->n > new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	trav = *head;
	while (1)
	{
		if (trav->next == NULL || trav->next->n > new->n)
		{
			new->next = trav->next;
			trav->next = new;
			return (new);
		}
		trav = trav->next;
	}
}
