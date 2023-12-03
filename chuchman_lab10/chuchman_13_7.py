filename = "text_13_7"

#A)------------------------------------> найдовше слово

def long_text(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        long_word = max(words, key=len)
        return long_word
result_1 = long_text(filename)
print(result_1)

#B)------------------------------------> кількість слів

def count_words(filename):
    with open(filename, 'r') as file:
        file_name = file.read()
        words = file_name.split()
        return len(words)
result_2 = count_words(filename)
print(result_2)

#C)------------------------------------> вилучення зайвих пропусків та всіх слів(з однієї букви)

def delete_words(filename):
    with open(filename, 'r') as file:
        file_name = file.read()
        words = file_name.split()

        cleaned_words = []
        for word in words:
            if len(word) > 2:
                cleaned_words.append(word)

        cleaned_file = [word for word in words if len(word) > 2]

    with open(filename, 'w') as file:
        delete_file = ' '.join(cleaned_file)
        file.write(delete_file)
    return " "

result_3 = delete_words(filename)
print(result_3)



