import re

def is_heading(line: str) -> bool:
    """
    Returns True if a line looks like a heading:
    - Mostly uppercase (ignores numbers & punctuation)
    - Or ends with a colon
    """
    # Rule 1: Ends with colon → heading
    if line.endswith(":"):
        return True

    # Extract only alphabetic characters
    letters = re.findall(r'[A-Za-z]', line)

    if not letters:  # No letters at all (e.g., "12345") → not a heading
        return False

    # Calculate ratio of uppercase letters
    uppercase_count = sum(1 for c in letters if c.isupper())
    ratio = uppercase_count / len(letters)

    # If at least 80% of letters are uppercase, consider it a heading
    return ratio >= 0.8


def clean_text(text: str) -> str:
    # ... (your earlier cleaning code here)

    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if is_heading(line):
            cleaned_lines.append("\n" + line + "\n")
        else:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines).strip()
