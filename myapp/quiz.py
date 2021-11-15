questions =[
    {"question":"①に当てはまるのは", "answer":"A"},
    {"question":"②にあてはまるのは", "answer":"A"},
    {"question":"③にあてはまるのは", "answer":"B"}
    ]

selection = [
    {"A":"鍵マーク", "B":"なにもはいらない"},
    {"A":"o", "B":"a"},
    {"A":"e", "B":"o"},
    ]

score = 0

for index in range(len(questions)):
    question = questions[index]['question']

    selectionA = selection[index]['A']
    selectionB = selection[index]['B']

    print("Q{0} {1}".format((index+1), question))
    print("A:{0} B:{1}".format(selectionA, selectionB))

    userInput = input ('回答を入力:')
    print("入力された値は {0} です" .format(userInput))

    if userInput.upper() == questions[index]['answer']:
        print("正解")

        score += 1
    else:
        print("{0}門中 {1}問正解。{2}点！おめでとう。".format(len(questions), score, score))
