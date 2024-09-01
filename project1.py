def increase_score(points):
    global score
    score += points


def add_body_part():
    global body_parts
    body_parts += 1


def print_stickman():
    stickman_parts = ["  O", "  |  ", " /  \\", "  |  ", " /  \\","  |  ", "/  \\","  |  ", "/  \\","  |  ", "/  \\"]
    print("Stickman:")
    for i in range(body_parts):
        print(stickman_parts[i])


greet = input("Are you ready for the game:")
user = input("✨Enter your name✨:")
print("Hello, " + user + " 🎉welcome🎉 to the world🌏 of stickman 웃")
need = input("Do you want some hints to play this game " + user + ":")
print("Tips💡:These are some tips to play this game\n"
      "👉 First you have guess the word with given hints\n"
      "👉 you have 9 chances to guess that word\n"
      "👉 For each chance you guess one letter of that word\n"
      "👉 For guessing one correct letter you can score 10 points and one body part of stickman 웃 is generated")
name = "butterfly"
score = 0
body_parts = 0

word = input("The word is ready do you want hints🤔:")
print("Hints:These are the some tips for guessing of the word\n"
      "📌 It is 9 letters word\n"
      "📌 It is an insect\n"
      "📌 That insect is very lovable for children\n"
      "📌 That insect contains several colours\n")

for chance in range(1, 10):
    letter = input(f"Chance {chance}:")
    if letter in name:
        print(f"Yes, {letter} is there in the name")
        increase_score(10)
        add_body_part()
    else:
        print("No")
    print_stickman()
    print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")

print("Your chances are over")
print("GAME OVER")
print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
points = input("Do you want to see your score🫣:")
print("Score:", score)
print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
print("Thank for playing game💐💐")
input("Do you want to play again:")
