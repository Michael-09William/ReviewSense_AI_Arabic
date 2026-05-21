import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from src.preprocessing import clean_text

model_path=r'C:\Users\10\OneDrive\Desktop\ReviewSense_AI\models\my_best_arabert_model_v79'

print("Loading Model AraBERT...")
try:
    tokenizer=AutoTokenizer.from_pretrained(model_path)
    model=AutoModelForSequenceClassification.from_pretrained(model_path)
    print('Laoding Done Successfully..')
except Exception as e:
    print(f'ERROR TYPE IS {e}')



def predict(text):

    inputs = tokenizer(
        text,
        return_tensors='pt',
        truncation=True,
        max_length=128
    ).to(model.device)

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.softmax(outputs.logits, dim=-1)
    label = torch.argmax(probs).item()
    labels_map = {0: '😤 سلبي', 1: '😊 ايجابي'}
    return labels_map[label], f"{probs[0][label].item():.2%}"




if __name__=='__main__':

    sentences = [
    "الكتاب ده رائع جداً",
    "الكتاب ده سيئ جدا",
    "المنتج وصل مكسور والجودة رديئة للغاية، لا أنصح به.",
    "تأخير غريب في الشحن ومحدش بيرد على التليفونات، خدمة زفت.",
    " كنت فاكره وحش لاني سمعت عنه كلام كتير بس التجربه خير دليل ولكن طلع شغال مفيهوش مشاكل نوعا ما (عادي)",
    "رحم الله العراب احمد خالد توفيق علي تعاليمه وقيمة التاركه لنا و جعل لدينا قدوة"
]

    print("🚀 نتائج التقييم:")
    print("-" * 50)

    for text in sentences:
        cleaned_text = clean_text(text)
        result, confidence = predict(cleaned_text)
        print(f"📝 النص: {text}")
        print(f"📊 النتيجة: {result} | 🔥 الثقة: {confidence}")
        print("-" * 50)
