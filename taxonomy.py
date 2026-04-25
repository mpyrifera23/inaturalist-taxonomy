import requests
from urllib.parse import quote

def lookup_inaturalist(common_name):
    """Look up using iNaturalist API"""
    url = f"https://api.inaturalist.org/v1/taxa/autocomplete?q={common_name}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        
        if data['results']:
            result = data['results'][0]
            scientific_name = result.get('name')
            if not scientific_name:
                return 'Not found'
            wiki_slug = scientific_name.replace(' ', '_')
            wiki_url = f"https://en.wikipedia.org/wiki/{quote(wiki_slug)}"
            return f"{scientific_name} ({wiki_url})"
        else:
            return 'Organism not found'
    except Exception as e:
        return f'Error: {e}'

while True:
    user_input = input("Enter a common name (or 'quit' to exit): ").strip()
    if user_input.lower() == 'quit':
        break
    
    result = lookup_inaturalist(user_input)
    print(f"Result: {result}\n")
