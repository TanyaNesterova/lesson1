school_scores =[
	{'school_class': '4a', 'score': [3,4,4,5,2]},
	{'school_class': '4r', 'score': [2,5,5,3,5]},
	{'school_class': '4y', 'score': [5,4,4,5,5]}
	]
school_sum = 0
school_len = 0
for class_scores in school_scores:
	print(class_scores)
	score = class_scores.get("score")
	print(score)
	class_name = class_scores.get("school_class")
	score_sum = sum(score)
	score_len = len(score)
	score_avg = score_sum/score_len
	print(f"средний балл по классу {class_name}: {score_avg}")
	school_sum += score_sum
	school_len += score_len
print(f"средний балл по школе: {school_sum/school_len}")
 
	