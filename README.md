CSV-Analyzer-CLI
A command-line interface (CLI) tool for analyzing bank statement data stored in CSV or JSON files. The tool provides insights into financial transactions through summaries, frequency analysis, net flow calculations, top transactions, histograms, and trend visualizations.
Features

Parse: Load a CSV/JSON file into memory for analysis.
Summary: Display total transactions, inflow, outflow, and net balance.
Frequency: Show transaction counts by description.
Net Flow: Calculate total inflow and outflow.
Top-K: List top transactions by amount or frequency.
Histogram: Generate a histogram of transaction amounts (saved as histogram.png).
Trend: Plot transaction trends over time (daily or monthly, saved as trend_daily.png or trend_monthly.png).
End: Discard loaded data to free up memory.

Installation
Prerequisites

Python 3.8 or higher
Virtual environment (recommended)
Git (optional, for version control)

Setup

Clone the Repository (if using Git):
git clone <https://github.com/Sonal-S-3009/CSV-Analyzer-CLI>
cd CSV-Analyzer-CLI


Create and Activate a Virtual Environment:
python -m venv venv


On Windows:venv\Scripts\activate


On Mac/Linux:source venv/bin/activate




Install Dependencies:
pip install pandas click matplotlib


Verify Setup:Ensure the virtual environment is activated and run:
python src/cli.py --help

This should display the available commands.


Usage
The CLI expects input files in CSV or JSON format with three columns: date (YYYY-MM-DD), description (text), and amount (numeric, positive for inflows, negative for outflows). A sample file, large_sample.csv, with 500 records is provided for testing.
Commands
Run commands from the project root with the virtual environment activated.

Parse a File:Load a CSV/JSON file into memory:
python src/cli.py parse large_sample.csv

Output: Displays the first 5 rows of the loaded data.

Summary:Show transaction summary:
python src/cli.py summary

Output: Total transactions, inflow, outflow, and net balance.

Frequency:Display transaction counts by description:
python src/cli.py frequency

Output: Number of occurrences for each description.

Net Flow:Calculate total inflow and outflow:
python src/cli.py net-flow

Output: Inflow and outflow amounts.

Top-K Transactions:List top transactions by amount or frequency:
python src/cli.py top-k --k 3 --by amount
python src/cli.py top-k --k 3 --by frequency

Output: Top 3 transactions sorted by amount or frequency.

Histogram:Generate a histogram of transaction amounts:
python src/cli.py histogram

Output: Saves histogram.png in the project root.

Trend:Plot transaction trends over time:
python src/cli.py trend --period daily
python src/cli.py trend --period monthly

Output: Saves trend_daily.png or trend_monthly.png.

End:Discard loaded data:
python src/cli.py end

Output: Confirms data has been discarded.


Example Workflow
python src/cli.py parse large_sample.csv
python src/cli.py summary
python src/cli.py top-k --k 5 --by frequency
python src/cli.py histogram
python src/cli.py trend --period monthly
python src/cli.py end

Project Structure
CSV-Analyzer-CLI/
├── venv/                    # Virtual environment
├── src/
│   ├── __init__.py
│   ├── cli.py              # Main CLI script
├── tests/                   # Directory for tests (empty)
├── sample.csv              # Original small sample CSV
├── temp_data.pkl           # Temporary file for loaded data (created/deleted by parse/end)
├── requirements.txt        # Dependencies (pandas, click, matplotlib)
├── histogram.png           # Output from histogram command
├── trend_daily.png         # Output from trend --period daily
├── trend_monthly.png       # Output from trend --period monthly
├── README.md               # This file
└── .gitignore              # Ignores venv, temp_data.pkl, etc.

Testing

Use sample.csv for testing:python src/cli.py parse sample.csv


Run all commands to verify outputs (e.g., check histogram.png and trend_*.png files).
Test error handling with a malformed CSV:
Edit large_sample.csv to add an invalid row (e.g., 2025,Invalid,abc).
Run parse and observe warnings about dropped rows.



Troubleshooting

"No such command" Error:
Use hyphens in command names (e.g., top-k, net-flow, not top_k, net_flow).
Run python src/cli.py --help to list valid commands.


"No data loaded" Error:
Run python src/cli.py parse large_sample.csv before analysis commands.


Date Parsing Errors:
Ensure the date column uses YYYY-MM-DD format.
The CLI skips invalid rows and warns about them.


Import Errors:
Verify dependencies: pip install pandas click matplotlib.
Ensure the virtual environment is activated.


Plot Issues:
Check for histogram.png or trend_*.png in the project root.
Ensure matplotlib is installed.



Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a feature branch (git checkout -b feature/new-feature).
Commit changes (git commit -m "Add new feature").
Push to the branch (git push origin feature/new-feature).
Open a pull request.

Please include tests in the tests/ directory and update this README if needed.
License
MIT License
Copyright (c) 2025 [Sonal Sinha]
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
<<<<<<< HEAD
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
=======
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
>>>>>>> 360ffded96375e87b6d4b3f19e4416e8e64dc9ed
