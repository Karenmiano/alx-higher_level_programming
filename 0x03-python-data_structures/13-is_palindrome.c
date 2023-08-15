#include "lists.h"
#include <stddef.h>
int is_palindrome(listint_t **head)
{
	listint_t *trav, *stay = *head;
	size_t num_nodes = 0, nodes, n;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	trav = *head;
	while(trav != NULL)
	{
		num_nodes++;
		trav = trav->next;
	}
	nodes = num_nodes;
	while(nodes > (num_nodes / 2))
	{
		for (n = nodes - 1, trav = *head; n != 0; n--)
		{
			trav = trav->next;
		}
		if (trav->n != stay->n)
			return (0);
		stay = stay->next;
		nodes--;
	}
	return (1);
}
