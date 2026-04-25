import requests
from urllib.parse import quote
import re

def lookup_inaturalist(common_name):
    """Look up using iNaturalist API"""
    url = "https://api.inaturalist.org/v1/taxa/autocomplete"
    try:
        response = requests.get(url, params={"q": common_name}, timeout=5)
        response.raise_for_status()
        data = response.json()

        results = data.get('results', [])
        if not results:
            return 'Organism not found'

        query = common_name.casefold()
        exact_match = None

        for result in results:
            candidate_terms = [
                result.get('matched_term'),
                result.get('preferred_common_name')
            ]
            if any(term and term.casefold() == query for term in candidate_terms):
                exact_match = result
                break

        if not exact_match:
            return "Invalid input: no exact common-name match found. Please check spelling."

        scientific_name = exact_match.get('name')
        if not scientific_name:
            return 'Not found'

        wiki_slug = scientific_name.replace(' ', '_')
        wiki_url = f"https://en.wikipedia.org/wiki/{quote(wiki_slug)}"
        return f"{scientific_name} ({wiki_url})"
    except Exception as e:
        return f'Error: {e}'

while True:
    user_input = input("Enter a common name (or 'quit' to exit): ").strip()
    if user_input.lower() == 'quit':
        break

    if not user_input:
        print("Result: Invalid input: please enter a common name.\n")
        continue

    if not re.fullmatch(r"[A-Za-z][A-Za-z\\s'\\-]*", user_input):
        print("Result: Invalid input: use letters, spaces, apostrophes, or hyphens only.\n")
        continue
    result = lookup_inaturalist(user_input)
    print(f"Result: {result}\n")
