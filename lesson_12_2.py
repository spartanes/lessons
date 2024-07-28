import re

def clean_html(input_file, output_file='cleaned.txt'):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        cleaned_content = re.sub(r'<[^>]*>', '', content)

        cleaned_content = '\n'.join([line for line in cleaned_content.splitlines() if line.strip()])

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)

        print(f"Очищений текст записано у файл: {output_file}")

    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")


clean_html('draft.html')
