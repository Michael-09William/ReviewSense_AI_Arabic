import re

def clean_text(text):

  text=re.sub(r'http\S+', '', text)

  text=re.sub(r'[أإآ]','ا',text)
  text=re.sub(r'[ة]','ه',text)
  text=re.sub(r'[ؤ]','ء',text)
  text=re.sub(r'[ئ]','ء',text)
  text=re.sub(r"ى", "ي",text)
  text = re.sub(r'(\w)\1{2,}', r'\1', text)
  text = re.sub(r'([^\w\s])\1+', r'\1', text)
  text = re.sub(r'[^\u0600-\u06FF\s\!\؟\.]', '', text)

  arabic_stopwords = [
        "انا", "انت", "او", "الي", "التي", "الذي", "ان", "بل", "ثم",
        "حيث", "حين", "ذلك", "عبر", "علي", "عن", "في", "لكن", "لم",
        "لن", "ما", "مع", "من", "هذا", "هذه", "هل", "هم", "هو", "هي", "يا",
        "انه", "انها", "انهم", "انك", "انني", "اننا", "فيها", "فيه", "عليهم", "عليه",
        "خالد", "احمد", "محمد", "محمود", "حسن", "عمر", "ساره", "فاطمه", "علي", "مصطفي",
        "مصر", "السعوديه", "الامارات", "الكويت", "قطر", "البحرين", "عمان",
        "العراق", "الاردن", "سوريا", "لبنان", "فلسطين", "اليمن", "ليبيا",
        "تونس", "الجزائر", "المغرب", "السودان", "الصومال", "جيبوتي", "موريتانيا" ]

  clean_word=[w for w in text.split() if w not in arabic_stopwords]

  return ' '.join(clean_word)






if __name__ == '__main__':

      #testing
      sample = "المطعم ده جميييييييييل جداً !!!!!!!! http://link.com"
      test_text = "ممتاااااااااااز جداااااااااا!!!!!!!!!!!! وينفع كدة.........؟؟؟؟؟؟؟؟"
      print(clean_text(sample))
      print(clean_text(test_text).split())
      print(clean_text(test_text))