for i in range(int(input())):
	min_count = 0
	max_count = 0
	s1 = input()
	s2 = input()
	for j in range(len(s1)):
		if s1[j] == '?' or s1[j] == '?':
			max_count += 1
		if s1[j] != s2[j]:
			min_count += 1
			max_count += 1
	min_count = str(min_count)
	max_count = str(max_count)
	print(min_count + " " +max_count)
