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
- Built-in error handling for API failures and timeouts (30-second timeout)

**Dependencies:**
- `requests` - For making HTTP requests to the iNaturalist API

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
   pip install requests
   ```

## Usage

Run the taxonomy lookup tool:

```bash
python taxonomy.py
```

Then enter common names at the prompt to look them up:

```
Enter a common name (or 'quit' to exit): robin
Result: Turdus migratorius

Enter a common name (or 'quit' to exit): quit
```

The tool will continue accepting input until you type `quit`.

## Contributing

Contributions and improvements are welcome! Feel free to fork, make changes, and submit pull requests.

## Author

- **mpyrifera23** - [GitHub Profile](https://github.com/mpyrifera23)

## Notes

This is an experimental/learning project. Code and functionality may change frequently as concepts are explored and tested.
