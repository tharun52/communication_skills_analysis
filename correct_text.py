import requests

def correct_grammar(text):
    # LanguageTool API endpoint
    api_url = "https://languagetool.org/api/v2/check"

    # Request headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    # Request payload
    data = {
        "text": text,
        "language": "en-US",
    }

    # Make the HTTP request
    response = requests.post(api_url, headers=headers, data=data)

    # Parse the JSON response
    json_response = response.json()

    # Extract corrected text from matches
    corrected_text = text
    for match in reversed(json_response.get("matches", [])):
        replacement = match.get("replacements", [{}])[0].get("value")
        if replacement:
            start = match["offset"]
            length = match["length"]
            corrected_text = corrected_text[:start] + replacement + corrected_text[start + length:]

    return corrected_text
