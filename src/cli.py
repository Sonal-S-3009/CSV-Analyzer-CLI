import click
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle
from datetime import datetime

# Path for temporary file to store DataFrame
TEMP_FILE = "temp_data.pkl"

def load_data(file_path):
    """Load CSV or JSON file into a pandas DataFrame."""
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format. Use CSV or JSON.")
        
        # Ensure required columns exist
        required_columns = ['date', 'description', 'amount']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("File must contain 'date', 'description', and 'amount' columns.")
        
        # Convert date column to datetime
        df['date'] = pd.to_datetime(df['date'])
        return df
    except Exception as e:
        click.echo(f"Error loading file: {str(e)}")
        return None

def save_data(df):
    """Save DataFrame to a temporary pickle file."""
    try:
        with open(TEMP_FILE, 'wb') as f:
            pickle.dump(df, f)
        return True
    except Exception as e:
        click.echo(f"Error saving data: {str(e)}")
        return False

def get_data():
    """Load DataFrame from temporary pickle file."""
    if not os.path.exists(TEMP_FILE):
        click.echo("No data loaded. Please run 'parse <file>' first.")
        return None
    try:
        with open(TEMP_FILE, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        click.echo(f"Error loading saved data: {str(e)}")
        return None

@click.group()
def cli():
    """CLI tool for analyzing bank statements and expenses."""
    pass

@cli.command()
@click.argument('file', type=click.Path(exists=True))
def parse(file):
    """Parse and load a CSV/JSON bank statement into memory."""
    df = load_data(file)
    if df is not None:
        if save_data(df):
            click.echo(f"Data loaded successfully from {file}:\n{df.head().to_string()}")

@cli.command()
def summary():
    """Display summary of transactions."""
    df = get_data()
    if df is not None:
        total_transactions = len(df)
        total_inflow = df[df['amount'] > 0]['amount'].sum()
        total_outflow = df[df['amount'] < 0]['amount'].abs().sum()
        net_balance = total_inflow - total_outflow
        click.echo(f"Summary:\n"
                   f"Total Transactions: {total_transactions}\n"
                   f"Total Inflow: ${total_inflow:.2f}\n"
                   f"Total Outflow: ${total_outflow:.2f}\n"
                   f"Net Balance: ${net_balance:.2f}")

@cli.command()
def frequency():
    """Show frequency of transactions by description."""
    df = get_data()
    if df is not None:
        freq = df['description'].value_counts()
        click.echo("Transaction Frequency by Description:\n")
        click.echo(freq.to_string())

@cli.command()
def net_flow():
    """Calculate net inflow and outflow."""
    df = get_data()
    if df is not None:
        inflow = df[df['amount'] > 0]['amount'].sum()
        outflow = df[df['amount'] < 0]['amount'].abs().sum()
        click.echo(f"Net Flow:\n"
                   f"Inflow: ${inflow:.2f}\n"
                   f"Outflow: ${outflow:.2f}")

@cli.command()
@click.option('--k', default=5, help='Number of top transactions to display')
@click.option('--by', type=click.Choice(['amount', 'frequency']), default='amount', help='Sort by amount or frequency')
def top_k(k, by):
    """Display top k transactions by amount or frequency."""
    df = get_data()
    if df is not None:
        if by == 'amount':
            top_transactions = df[['description', 'amount']].nlargest(k, 'amount')
            click.echo(f"Top {k} Transactions by Amount:\n{top_transactions.to_string()}")
        else:
            freq = df['description'].value_counts().head(k)
            click.echo(f"Top {k} Transactions by Frequency:\n{freq.to_string()}")

@cli.command()
def histogram():
    """Generate and save a histogram of transaction amounts."""
    df = get_data()
    if df is not None:
        plt.figure(figsize=(10, 6))
        plt.hist(df['amount'], bins=20, edgecolor='black')
        plt.title('Histogram of Transaction Amounts')
        plt.xlabel('Amount ($)')
        plt.ylabel('Frequency')
        output_file = 'histogram.png'
        plt.savefig(output_file)
        plt.close()
        click.echo(f"Histogram saved as {output_file}")

@cli.command()
@click.option('--period', type=click.Choice(['daily', 'monthly']), default='daily', help='Trend period (daily or monthly)')
def trend(period):
    """Generate and save a trend plot of transactions over time."""
    df = get_data()
    if df is not None:
        if period == 'daily':
            df = df.copy()
            df['date_trunc'] = df['date'].dt.date
            trend_data = df.groupby('date_trunc')['amount'].sum()
        else:  # monthly
            df = df.copy()
            df['date_trunc'] = df['date'].dt.to_period('M').dt.to_timestamp()
            trend_data = df.groupby('date_trunc')['amount'].sum()
        
        plt.figure(figsize=(12, 6))
        trend_data.plot()
        plt.title(f'Transaction Trend ({period.capitalize()})')
        plt.xlabel('Date')
        plt.ylabel('Total Amount ($)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        output_file = f'trend_{period}.png'
        plt.savefig(output_file)
        plt.close()
        click.echo(f"Trend plot saved as {output_file}")

@cli.command()
def end():
    """Discard the loaded data."""
    if os.path.exists(TEMP_FILE):
        try:
            os.remove(TEMP_FILE)
            click.echo("Loaded data has been discarded.")
        except Exception as e:
            click.echo(f"Error discarding data: {str(e)}")
    else:
        click.echo("No data loaded to discard.")

if __name__ == '__main__':
    cli()