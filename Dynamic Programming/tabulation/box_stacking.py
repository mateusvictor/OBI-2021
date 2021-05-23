def tallest_stack(boxes):
	boxes.sort(key=lambda x:x[0]) # sorting by length
	print(boxes)
	heights = {box: box[2] for box in boxes}

	for i in range(1, len(boxes)):
		box = boxes[i]
		subproblems = [heights[boxes[j]] for j in range(i) if can_be_stacked(boxes[j], box)]
		heights[box] = box[2] + max(subproblems, default=0)

	return max(heights.values(), default=0)

def can_be_stacked(top, bottom):
	return top[0] < bottom[0] and top[1] < bottom[1]


boxes = [(4, 5, 3), (2, 3, 2), (3, 6, 2), (1, 5, 4), (2, 4, 1), (1, 2, 2)]
print(tallest_stack(boxes))