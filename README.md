# Maxi Supermarket Price Extractor

This project contains Python scripts to interact with the Maxi (a Canadian supermarket chain) website's underlying API to fetch product information.

## Scripts

*   `maxi_autocomplete.py`: Provides product suggestions based on a search term using the type-ahead API endpoint.
*   `maxi_wrapper.py`: Searches for products based on a term and desired number of results, then displays their brand, name, and price.

## Requirements

*   Python 3.x
*   requests library

## Installation

1.  Clone this repository (if you haven't already).
2.  Navigate to the project directory in your terminal.
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the scripts from your terminal:

*   **Autocomplete:**
    ```bash
    python maxi_autocomplete.py
    ```
    The script will prompt you interactively: "On cherche quoi?" (What are we looking for?). Enter your search term and press Enter. The raw JSON response from the API will be printed. Press Ctrl+C to exit.

*   **Product Search:**
    ```bash
    python maxi_wrapper.py
    ```
    The script will prompt you interactively:
    1.  "Combien de résultats voulez-vous?" (How many results do you want?) - Enter a number.
    2.  "On cherche quoi?" (What are we looking for?) - Enter your search term.
    The script will then print a table of the found products with their brand, name, and price. Press Ctrl+C to exit the loop.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.