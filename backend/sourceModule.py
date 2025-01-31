different_letter = {'я':'йа',
                    'ю':'йу',
                    'ё':'йо'}
def replace_letter(word):
    for letter in word:
        if letter in different_letter:
            word = word.replace(letter, str(different_letter.get(letter)))
    return word

posessiveness_general = {
    'ны', 'ни', 'ну', 'нү',
    'ды', 'ди', 'ду', 'дү',
    'ты', 'ти', 'ту', 'тү'
}
noun = {
    "коён", "аюу", "балык", "бал", "алма", "мал", "кыргызстан", "жол", "ал"
}
verb = {
    'ал', 'кыл','отур', 'тайгалан', 'кыл', 'айлан', 'айт', 'алмаш'
}
adjective = {
"адабий", "адал", "боз",'кызыл', 'сары', 'жашыл', 'ак', 'жакшы', 'жаман', 'сулуу', "чоң", "кичине","чын",'ачуу'
}

case = ['gen','dat','acc','loc','abl']
voice = ['ref','coop','pass','caus']
mood = ['ind_pres','ind_past','ind_fut','cnd','niet','tilek']
face = ['p1sg','p1pl','p2sg','p2pl']
consonants_kg = {
    'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'ң', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'
}
special_vowel = {
    'и', 'ы', 'у', 'ү'
}
vowels_kg = {
    'а', 'о', 'ө', 'э', 'и', 'ы', 'у', 'ү', 'аа', 'оо', 'өө', 'ээ', 'уу', 'үү', 'я', 'ю', 'ё', 'е'
}
all_punctuation_marks = ['.',',','?','!','"',';',':','{','}','`']
sentence_end_p_m = ['. ','! ','? ']


