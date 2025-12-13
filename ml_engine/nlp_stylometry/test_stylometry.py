from ml_engine.nlp_stylometry import (
    PunctuationProfile,
    VocabularyProfile,
    SyntaxRhythm,
    SemanticEmbedding,
    StylometryEngine
)

# --- Fake user texts ---
user_a = [
    "This is amazing!!! I really love this project 😃",
    "Honestly, this works really well. Great job!"
]

user_b = [
    "This is amazing!!! I really love this project 😃",
    "Honestly, this works really well. Great job!"
]

user_c = [
    "Check crypto now pump soon",
    "BUY NOW!!! PROFIT FAST!!!"
]

def build_profile(texts):
    punc = PunctuationProfile().extract(texts)
    vocab = VocabularyProfile().build_profile(texts)
    syntax = SyntaxRhythm().build_profile(texts)
    semantic = SemanticEmbedding().embed(texts)

    return {
        "punctuation": punc,
        "tfidf": vocab["tfidf"],
        "uniqueness": vocab["uniqueness"],
        "syntax": syntax,
        "semantic": semantic,
    }

profile_a = build_profile(user_a)
profile_b = build_profile(user_b)
profile_c = build_profile(user_c)

engine = StylometryEngine()

print("\nA vs B (same style)")
print(engine.compare(profile_a, profile_b))

print("\nA vs C (different style)")
print(engine.compare(profile_a, profile_c))
