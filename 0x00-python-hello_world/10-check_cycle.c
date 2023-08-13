#include "lists.h"
/**
 * check_cycle - checks if there's a cycle in a singly linked list
 * @list: address of node to start checking from
 * Return: 0 if no cycle is found, 1 if one is found
 */
int check_cycle(listint_t *list)
{
	listint_t **addrs, **addrs2;
	int i, j;

	if (list == NULL)
		return (0);
	addrs = malloc(sizeof(listint_t *));
	addrs[0] = NULL;
	while (list != NULL)
	{
		for (i = 0; addrs[i] != NULL; i++)
		{
			if (addrs[i] == list)
			{
				free(addrs);
				return (1);
			}
		}
		addrs2 = malloc(sizeof(listint_t *) * (i + 2));
		addrs2[0] = list;
		for (i = 1, j = 0; addrs[j] != NULL; i++, j++)
			addrs2[i] = addrs[j];
		addrs2[i] = NULL;
		free(addrs);
		addrs = addrs2;
		list = list->next;
	}
	free(addrs);
	return (0);
}
