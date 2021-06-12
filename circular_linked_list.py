def is_circular_linked_list(self, input_list):
	cur=input_list.head
	while cur:
		cur=cur.next
		if cur==input_list.head:
			return True
	return False



