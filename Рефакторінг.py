import PySimpleGUI as sg
import random

class WordGenerator:
    @staticmethod
    def choose_random_word():
        words = ["яблуко", "абрикос", "апельсин", "банан", "персик", "лимон", "слива", "груша", "полуниця", "ківі"]
        return random.choice(words)

class WordGame:
    def __init__(self, max_attempts=5):
        self.max_attempts = max_attempts
        self.target_word = WordGenerator.choose_random_word()

    def display_word(self, guessed_word):
        return " ".join(guessed_word)

    def display_attempts(self):
        return f"Залишилося спроб: {self.max_attempts - self.attempts}"

    def play_game(self):
        self.attempts = 0
        guessed_word = ["_"] * len(self.target_word)

        layout = [
            [sg.Text(self.display_word(guessed_word), key="word_display", size=(30, 1), justification="center")],
            [sg.Text(self.display_attempts(), key="attempts_display")],
            [sg.InputText(key="user_input", size=(15, 1)), sg.Button("Guess"), sg.Button("Exit")]
        ]

        window = sg.Window("Guess the Word", layout, element_justification="center")

        while self.attempts < self.max_attempts:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Exit":
                break

            user_guess = values["user_input"].strip().lower()

            if user_guess == self.target_word:
                sg.popup_ok(f"Ви вгадали слово '{self.target_word}' за {self.attempts + 1} спроб!")
                break
            else:
                self.attempts += 1
                guessed_word = ["_" if letter != user_guess else letter for letter in self.target_word]
                window["word_display"].update(self.display_word(guessed_word))
                window["attempts_display"].update(self.display_attempts())

        if self.attempts >= self.max_attempts:
            sg.popup_ok(f"Ви вичерпали всі спроби. Правильне слово було '{self.target_word}'.")

        window.close()

if __name__ == "__main__":
    sg.theme("LightGreen4")

    print("Гра 'Вгадайте слово!'")
    print("Фрукти, які ви можете вибрати: яблуко, абрикос, апельсин, банан, персик, лимон, слива, груша, полуниця, ківі")

    game = WordGame()
    game.play_game()
