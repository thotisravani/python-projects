user=input("Enter your name👉:")
print("Welcome to the game show 💸💸who want to be a millionaire💸💸")
print("***************************************************************************")
input(" ")
print("👉Here,you can get some money for the correct answer of each question\n"
      "👉So play carefully and tell the answer carefully\n")
print("👉If you tell wrong answer in any question on that point your should be stopped")
print("***************************************************************************")
input(" ")
print("All the best💐💐",user)
input("start")
print("***************************************************************************")
questions = [
    ("What is the capital of France?", ("A. Paris", "B. London", "C. Rome", "D. Berlin", "A", 10000)),
    ("Which planet is known as the Red Planet?", ("A. Venus", "B. Jupiter", "C. Mars", "D. Saturn", "C", 20000)),
    ("Who wrote 'Romeo and Juliet'?", ("A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain", "B", 30000)),
    ("What is the chemical symbol for water?", ("A. H2O2", "B. CO2", "C. H2O", "D. CH4", "C", 50000)),
    ("What is the largest mammal in the world?", ("A. Elephant", "B. Giraffe", "C. Blue Whale", "D. Lion", "C", 100000)),
    ("Which of these countries is not in Europe?", ("A. France", "B. Germany", "C. Brazil", "D. Italy", "C", 200000)),
    ("Which gas do plants need to perform photosynthesis?", ("A. Nitrogen", "B. Oxygen", "C. Carbon dioxide", "D. Hydrogen", "C", 300000)),
    ("Who painted the Mona Lisa?", ("A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Michelangelo", "B", 500000)),
    ("Which year did the Titanic sink?", ("A. 1912", "B. 1920", "C. 1905", "D. 1899", "A", 1000000)),
    ("What is the chemical symbol for gold?", ("A. Go", "B. Au", "C. Ag", "D. Hg", "B", 2500000)),
    ("Which bird is known for its ability to mimic human speech?", ("A. Crow", "B. Parrot", "C. Eagle", "D. Pigeon", "B", 5000000)),
    ("Which planet is closest to the Sun?", ("A. Venus", "B. Mars", "C. Mercury", "D. Earth", "C", 75000000)),
    ("Who is known as the 'Father of Computer'?", ("A. Bill Gates", "B. Alan Turing", "C. Steve Jobs", "D. Tim Berners-Lee", "B", 8000000)),
    ("What is the chemical symbol for iron?", ("A. Ir", "B. Fe", "C. Au", "D. Ag", "B", 9000000)),
    ("Which country is known as the Land of the Rising Sun?", ("A. China", "B. Japan", "C. South Korea", "D. Thailand", "B", 95000000)),
    ("Who discovered penicillin?", ("A. Alexander Fleming", "B. Louis Pasteur", "C. Marie Curie", "D. Albert Einstein", "A", 10000000)),
]

def ask_question(question, options, correct_answer, amount):
    print(question)
    for option in options:
        print(option)
    return correct_answer, amount

def play_game():
    money = 0
    print("Welcome to Who Wants to Be a Millionaire?")
    for question, (option1, option2, option3, option4, correct_answer, amount) in questions:
        correct_answer, amount = ask_question(question, (option1, option2, option3, option4), correct_answer, amount)
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        if user_answer == correct_answer:
            print(f"Correct! You've won ${amount}!")
            money += amount
        else:
            print(f"Sorry, the correct answer was {correct_answer}. You won ${money}.")
            break
    else:
        print("Congratulations! You've won $1,000,000!💐💐💐💐")

play_game()
