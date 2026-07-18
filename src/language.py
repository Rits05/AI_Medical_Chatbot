from langdetect import detect


def detect_language(text):
    try:
        lang = detect(text)

        if lang == "hi":
            return "Hindi"

        if lang == "en":
            hinglish_words = [
                "kya", "hai", "mera", "mujhe",
                "kaise", "kitna", "kab",
                "kyun", "mein", "aur",
                "hota", "hoti", "karna"
            ]

            text = text.lower()

            if any(word in text.split() for word in hinglish_words):
                return "Hinglish"

            return "English"

    except:
        pass

    return "English"