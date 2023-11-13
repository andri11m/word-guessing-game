import PySimpleGUI as sg
import random

def choose_random_word():
    words = ["яблуко", "абрикос", "апельсин", "банан", "персик", "лимон", "слива", "груша", "полуниця", "ківі"]
    return random.choice(words)

def guess_word(target_word, max_attempts=5):
    attempts = 0
    guessed_word = ["_"] * len(target_word)

    layout = [
        [sg.Text(" ".join(guessed_word), key="word_display", size=(30, 1), justification="center")],
        [sg.Text(f"Залишилося спроб: {max_attempts - attempts}", key="attempts_display")],
        [sg.InputText(key="user_input", size=(15, 1)), sg.Button("Guess"), sg.Button("Exit")]
    ]

    window = sg.Window("Guess the Word", layout, element_justification="center")

    while attempts < max_attempts:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break

        user_guess = values["user_input"].strip().lower()

        if user_guess == target_word:
            sg.popup_ok(f"Ви вгадали слово '{target_word}' за {attempts + 1} спроб!")
            break
        else:
            attempts += 1
            guessed_word = ["_" if letter != user_guess else letter for letter in target_word]
            window["word_display"].update(" ".join(guessed_word))
            window["attempts_display"].update(f"Залишилося спроб: {max_attempts - attempts}")

    if attempts >= max_attempts:
        sg.popup_ok(f"Ви вичерпали всі спроби. Правильне слово було '{target_word}'.")

    window.close()

# Новий функціонал інтерфейсу
def show_instructions():
    sg.popup("Гра 'Вгадайте слово!'\n\nІнструкції:\n1. Вгадайте слово зі списку фруктів.\n2. Введіть слово через інтерфейс.\n3. Спробуйте вгадати за обмежену кількість спроб.")

if __name__ == "__main__":
    sg.theme("LightGreen4")

    print("Гра 'Вгадайте слово!'")
    print("Фрукти, які ви можете вибрати: яблуко, абрикос, апельсин, банан, персик, лимон, слива, груша, полуниця, ківі")

    target_word = choose_random_word()
    guess_word(target_word)

    # Додано новий функціонал інтерфейсу - показ інструкцій
    show_instructions()
