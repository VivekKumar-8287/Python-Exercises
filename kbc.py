# KBC Game

questions = [
    ['Which god is also known as \"Gauri Nandan\" ?','Agni','Indra','Hanuman','Ganesha','None',4],
    ['What does not grow on tree according to a popular Hindi saying?','Money','Flowers','Leaves','Fruits','None',4],
    ['Which city is known as Pink City in India?','Banglore','Maysore','Jaipur','Kochi','None',4],
    ['Who wrote India\'s National Anthem?','Rabindranath Tagore','Lal Bahadur Shastri','Chetan Bhagat','RK Narayan','None',4],
    ['When is the National Hindi Diwas celebrated?','13 September','14 September','14 July','15 August','None',4],
    ['The largest Buddhist Monastery in India is located at','Sarnath, Uttar Pradesh','Tawang, Arunachal Pradesh','Dharmshala, Himachal Pradesh','Gangtok, Sikkim','None',4],
    ['Which former Indian President died as a result of a road accident?','Rajendra Prasad','Faqruddin Ali Ahmed','Giani Zail Singh','R.Venkatraman','None',4],
    ['Who was the first Indian woman to win a medal in the Olympics?','P.T. Usha','Kunjarani Devi','Bachendri Pal','Karnam Maleshwari','None',4],
    ['Which Mughal Emperor was deported to Rangoon by the British?','Shah Jahan','Bahadur Shah II','Akbar Shah I','Bahadur Shah I','None',4],
]

levels = [1000,2000,3000,5000,10000,40000,80000,160000,3200000]
money = 0

for i in range(0,len(questions)):
    question = questions[i]
    print(f'\n\nQuestion for Rs. {levels[i]}')
    print(f'{question[i]}')
    print(f'a. {question[1]}       b. {question[2]}')
    print(f'c. {question[3]}       d. {question[4]}')
    reply = int(input("Enter your answer (1-4)"))
    if(reply == question[-1]):
        print(f'Correct answer, you have won Rs. {levels[i]}')
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print('Wrong answer!')
        break

print(f'Your take home money is {money}')