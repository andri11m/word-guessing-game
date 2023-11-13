<<<<<<< HEAD
import PySimpleGUI as sg
from game_logic import choose_random_word, guess_word

# Додамо можливість гравцю вводити слово для вгадування
def custom_guess():
    layout = [
        [sg.Text("Введіть слово для вгадування: "), sg.InputText(key='input_word')],
        [sg.Button("Вгадати"), sg.Button("Вийти")]
    ]

    window = sg.Window("Спробуйте вгадати слово", layout)

    while True:
        event, values = window.read()

        if event in (None, 'Вийти'):
            break
        if event == 'Вгадати':
            guessed_word = values['input_word'].strip()
            result = "Правильно!" if guessed_word == target_word else "Спробуйте ще раз."
            sg.popup(result)

    window.close()

if __name__ == "__main__":
    sg.theme("LightGreen4")

    print("Гра 'Вгадайте слово!'")
    print("Фрукти, які ви можете вибрати: яблуко, абрикос, апельсин, банан, персик, лимон, слива, груша, полуниця, ківі")

    target_word = choose_random_word()

    # Викличемо нову функцію для вгадування слів
    custom_guess()
=======
import PySimpleGUI as sg
from game_logic import choose_random_word, guess_word

# Додамо можливість гравцю вводити слово для вгадування
def custom_guess():
    layout = [
        [sg.Text("Введіть слово для вгадування: "), sg.InputText(key='input_word')],
        [sg.Button("Вгадати"), sg.Button("Вийти")]
    ]

    window = sg.Window("Спробуйте вгадати слово", layout)

    while True:
        event, values = window.read()

        if event in (None, 'Вийти'):
            break
        if event == 'Вгадати':
            guessed_word = values['input_word'].strip()
            result = "Правильно!" if guessed_word == target_word else "Спробуйте ще раз."
            sg.popup(result)

    window.close()

if __name__ == "__main__":
    sg.theme("LightGreen4")

    print("Гра 'Вгадайте слово!'")
    print("Фрукти, які ви можете вибрати: яблуко, абрикос, апельсин, банан, персик, лимон, слива, груша, полуниця, ківі")

    target_word = choose_random_word()

    # Викличемо нову функцію для вгадування слів
    custom_guess()
>>>>>>> origin/main
