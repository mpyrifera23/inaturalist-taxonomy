# iNaturalist Taxonomy

## Overview

This is a repo containing a Python-based taxonomy lookup tool that integrates with the iNaturalist API.

## Language

- **Python** (100%)

## Features

### Taxonomy Lookup Tool (`taxonomy.py`)

A command-line utility that looks up organism information using the iNaturalist API.

**Functionality:**
- Search for organisms by common name
- Query the iNaturalist API (`https://api.inaturalist.org/v1/taxa/autocomplete`)
- Returns the scientific or official name of the organism
- Interactive loop for multiple lookups
- Validates user input (non-empty and letters/spaces/apostrophes/hyphens only)
- Requires an exact common-name match from API results to avoid incorrect fuzzy matches
- Built-in error handling for API failures and timeouts (5-second timeout)

**Dependencies:**
- `requests` - For making HTTP requests to the iNaturalist API

### COMING SOON: Fish Taxonomy Identification Game ('fishgame.py')

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mpyrifera23/inaturalist-taxonomy.git
   cd inaturalist-taxonomy
   ```

2. Install dependencies:
   ```bash
   pip3 install requests
   ```

## Usage

Run the taxonomy lookup tool:

```bash
python3 taxonomy.py
```

Then enter common names at the prompt to look them up:

```
Enter a common name (or 'quit' to exit): robin
Result: Erithacus rubecula (https://en.wikipedia.org/wiki/Erithacus_rubecula)

Enter a common name (or 'quit' to exit): quit
```

The tool will continue accepting input until you type `quit`.

If input is invalid, the tool returns clear validation messages:

```
Enter a common name (or 'quit' to exit): 
Result: Invalid input: please enter a common name.

Enter a common name (or 'quit' to exit): robin!
Result: Invalid input: use letters, spaces, apostrophes, or hyphens only.

Enter a common name (or 'quit' to exit): quir
Result: Invalid input: no exact common-name match found. Please check spelling.
```

## Contributing

Contributions and improvements are welcome! Feel free to fork, make changes, and submit pull requests.

## Author

- **mpyrifera23** - [GitHub Profile](https://github.com/mpyrifera23)

## Notes

This is an experimental/learning project. Code and functionality may change frequently as concepts are explored and tested.
