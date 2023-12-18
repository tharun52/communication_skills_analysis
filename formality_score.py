import spacy

def calculate_formality_score(text):
    # Load the spaCy English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text using spaCy
    doc = nlp(text)

    # Count formal and total words
    formal_words = 0
    total_words = 0

    for token in doc:
        # Consider only non-stop words
        if not token.is_stop:
            total_words += 1
            # Check if the word is considered formal (you can customize this condition)
            if token.pos_ in ["NOUN", "PROPN", "VERB"]:
                formal_words += 1

    # Calculate formality score
    formality_score = formal_words / total_words if total_words > 0 else 0

    return formality_score

if __name__ == "__main__":
    # Example usage
    input_text = "I earnestly request your kind consideration of the matter at hand and seek your esteemed approval for the proposed budget allocation in the forthcoming fiscal year."
    score = calculate_formality_score(input_text)
    print(f"Formality Score: {score}")
