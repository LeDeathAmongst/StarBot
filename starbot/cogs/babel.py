import os
import subprocess
from googletrans import Translator

# Comprehensive list of language codes
LANGUAGES = [
    'af', 'ar', 'bg', 'bn', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'et',
    'fa', 'fi', 'fr', 'he', 'hi', 'hr', 'hu', 'id', 'it', 'ja', 'ko', 'lt',
    'lv', 'ms', 'nl', 'no', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'sv', 'th',
    'tr', 'uk', 'vi', 'zh-cn', 'zh-tw'
]

def translate_po_file(po_file, lang):
    translator = Translator()
    with open(po_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    translated_lines = []
    for line in lines:
        if line.startswith('msgid "'):
            translated_lines.append(line)
            msgstr = line.strip()[7:-1]  # Extract the string to translate
            if msgstr:
                translation = translator.translate(msgstr, dest=lang).text
                translated_lines.append(f'msgstr "{translation}"\n')
            else:
                translated_lines.append('msgstr ""\n')
        else:
            translated_lines.append(line)

    with open(po_file, 'w', encoding='utf-8') as f:
        f.writelines(translated_lines)

def run_pybabel_commands(directory):
    print(f"Processing directory: {directory}")
    os.chdir(directory)

    if not os.path.exists('locales'):
        os.makedirs('locales')

    extract_command = ['pybabel', 'extract', '-o', 'locales/messages.pot', '.']
    try:
        subprocess.run(extract_command, check=True)
        print(f"Extraction successful in {directory}")
    except subprocess.CalledProcessError as e:
        print(f"Extraction error in {directory}: {e}")
        return

    for lang in LANGUAGES:
        lang_dir = os.path.join('locales', lang, 'LC_MESSAGES')
        if not os.path.exists(lang_dir):
            os.makedirs(lang_dir)

        po_file = os.path.join(lang_dir, 'messages.po')
        if os.path.exists(po_file):
            update_command = ['pybabel', 'update', '-i', 'locales/messages.pot', '-d', 'locales', '-l', lang]
        else:
            update_command = ['pybabel', 'init', '-i', 'locales/messages.pot', '-d', 'locales', '-l', lang]

        try:
            subprocess.run(update_command, check=True)
            print(f"Updated/Initialized translations for {lang} in {directory}")
            translate_po_file(po_file, lang)
            print(f"Automatically translated {lang} in {directory}")
        except subprocess.CalledProcessError as e:
            print(f"Error for {lang} in {directory}: {e}")

def process_directories(start_dir):
    start_dir_abs = os.path.abspath(start_dir)
    subdirs = [d for d in os.listdir(start_dir_abs) if os.path.isdir(os.path.join(start_dir_abs, d))]

    for subdir in subdirs:
        full_path = os.path.join(start_dir_abs, subdir)
        run_pybabel_commands(full_path)

if __name__ == "__main__":
    start_directory = "."
    process_directories(start_directory)
