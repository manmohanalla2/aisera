def reverse(sentence):
	lst_sentence = sentence.split(" ")
	r_string = ""
	r_string = ' '.join(lst_sentence[::-1])
	return r_string
print(reverse("hi how are u"))