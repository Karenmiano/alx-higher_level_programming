#include "lists.h"
/**
 * print_dlistint - function that prints the elements of a doubly
 * linked list
 * @h: pointer to the head node
 * Return: number of nodes in the list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t nodes = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		nodes++;
	}
	return (nodes);
}
