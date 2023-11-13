<<<<<<< HEAD
# Модуль для роботи з конфігураційними файлами
import configparser

# Функція для зчитування налаштувань з файлу
def read_settings():
    config = configparser.ConfigParser()
    try:
        config.read('config.ini')  # Назва файлу конфігурації
        settings = {
            'max_attempts': int(config.get('GameSettings', 'max_attempts', fallback=5))  # Зчитуємо максимальну кількість спроб
        }
    except (configparser.NoSectionError, configparser.NoOptionError, ValueError):
        settings = {'max_attempts': 5}  # Значення за замовчуванням
    return settings

# Функція для запису налаштувань у файл
def write_settings(settings):
    config = configparser.ConfigParser()
    config['GameSettings'] = {
        'max_attempts': str(settings['max_attempts'])
    }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

# Викликаємо функції для зчитування та запису налаштувань
if __name__ == "__main__":
    settings = read_settings()
    print(f"Поточні налаштування: {settings}")

    # Можна змінити налаштування
    settings['max_attempts'] = 10
    write_settings(settings)
    print(f"Нові налаштування: {settings}")
=======
# Модуль для роботи з конфігураційними файлами
import configparser

# Функція для зчитування налаштувань з файлу
def read_settings():
    config = configparser.ConfigParser()
    try:
        config.read('config.ini')  # Назва файлу конфігурації
        settings = {
            'max_attempts': int(config.get('GameSettings', 'max_attempts', fallback=5))  # Зчитуємо максимальну кількість спроб
        }
    except (configparser.NoSectionError, configparser.NoOptionError, ValueError):
        settings = {'max_attempts': 5}  # Значення за замовчуванням
    return settings

# Функція для запису налаштувань у файл
def write_settings(settings):
    config = configparser.ConfigParser()
    config['GameSettings'] = {
        'max_attempts': str(settings['max_attempts'])
    }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

# Викликаємо функції для зчитування та запису налаштувань
if __name__ == "__main__":
    settings = read_settings()
    print(f"Поточні налаштування: {settings}")

    # Можна змінити налаштування
    settings['max_attempts'] = 10
    write_settings(settings)
    print(f"Нові налаштування: {settings}")
>>>>>>> origin/main
