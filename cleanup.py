import re

# Task: Clean text by removing special characters/images placeholders

def clean_text(text):
    # Remove weird symbols (keep letters, numbers, punctuation)
    text = re.sub(r"[^a-zA-Z0-9\s.,;:!?'\-\n]", "", text)
    
    # Remove multiple spaces/newlines
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

if __name__ == "__main__":
    raw_text = "e   ©   [| Square SA .@ He • aa lS Z\ Triangle Orang r*) ?"
    cleaned = clean_text(raw_text)
    print("Before:\n", raw_text)
    print("After:\n", cleaned)
