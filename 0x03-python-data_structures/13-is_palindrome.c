#include "lists.h"
/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome | 0 if not palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *t_h = *head, *tail = *head, *aux = *head;

	if (*head == NULL)
		return (1);
	while (tail->next != NULL)
		tail = tail->next;
	while (t_h->next != tail && t_h != tail)
	{
		aux = *head;
		if (t_h->n == tail->n)
		{
			t_h = t_h->next;
			while (aux->next != tail)
				aux = aux->next;
			tail = aux;
		}
		else
			return (0);
	}
	return (1);
}
