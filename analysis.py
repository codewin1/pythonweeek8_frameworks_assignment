"""
CORD-19 Dataset Analysis
Simple version with essential analysis only
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from pathlib import Path

class SimpleAnalyzer:
    def __init__(self, data_path="data/metadata.csv"):
        self.data_path = data_path
        self.df = None
        
        # Create output directories
        Path("results").mkdir(exist_ok=True)
        Path("results/visualizations").mkdir(exist_ok=True)
    
    def load_data(self, sample_size=15000):
        """Load dataset"""
        print(f"Loading data from {self.data_path}...")
        
        if not os.path.exists(self.data_path):
            print(f"Error: File not found - {self.data_path}")
            return False
        
        try:
            self.df = pd.read_csv(self.data_path, nrows=sample_size)
            print(f"Loaded {len(self.df):,} records")
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def clean_data(self):
        """Clean dataset"""
        print("Cleaning data...")
        initial_count = len(self.df)
        
        # Convert dates
        if 'publish_time' in self.df.columns:
            self.df['publish_time'] = pd.to_datetime(self.df['publish_time'], errors='coerce')
            self.df['year'] = self.df['publish_time'].dt.year
            
            # Filter years
            self.df = self.df[(self.df['year'] >= 1990) & (self.df['year'] <= 2024) | self.df['year'].isna()]
        
        # Calculate text lengths
        if 'title' in self.df.columns:
            self.df['title_length'] = self.df['title'].fillna('').str.len()
        
        if 'abstract' in self.df.columns:
            self.df['abstract_length'] = self.df['abstract'].fillna('').str.len()
        
        # Remove empty records
        if 'title' in self.df.columns and 'abstract' in self.df.columns:
            self.df = self.df[(self.df['title'].notna()) | (self.df['abstract'].notna())]
        
        print(f"Cleaned dataset: {len(self.df):,} records ({initial_count - len(self.df):,} removed)")
    
    def create_visualizations(self):
        """Create analysis visualizations"""
        print("Creating visualizations...")
        
        plt.style.use('default')
        
        # 1. Publications by year
        if 'year' in self.df.columns:
            year_counts = self.df['year'].value_counts().sort_index()
            
            plt.figure(figsize=(10, 6))
            year_counts.plot(kind='bar', color='steelblue')
            plt.title('Publications by Year')
            plt.xlabel('Year')
            plt.ylabel('Number of Publications')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('results/visualizations/publication_trends.png', dpi=300, bbox_inches='tight')
            plt.close()
        
        # 2. Top journals
        if 'journal' in self.df.columns:
            journal_counts = self.df['journal'].value_counts().head(15)
            
            plt.figure(figsize=(12, 8))
            journal_counts.plot(kind='barh', color='coral')
            plt.title('Top 15 Journals')
            plt.xlabel('Number of Publications')
            plt.tight_layout()
            plt.savefig('results/visualizations/top_journals.png', dpi=300, bbox_inches='tight')
            plt.close()
        
        # 3. Text analysis
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        if 'title_length' in self.df.columns:
            self.df['title_length'][self.df['title_length'] > 0].hist(bins=30, ax=axes[0], alpha=0.7)
            axes[0].set_title('Title Length Distribution')
            axes[0].set_xlabel('Characters')
            axes[0].set_ylabel('Frequency')
        
        if 'abstract_length' in self.df.columns:
            abstract_lengths = self.df['abstract_length'][self.df['abstract_length'] > 0]
            abstract_lengths.hist(bins=30, ax=axes[1], alpha=0.7)
            axes[1].set_title('Abstract Length Distribution')
            axes[1].set_xlabel('Characters')
            axes[1].set_ylabel('Frequency')
        
        plt.tight_layout()
        plt.savefig('results/visualizations/text_analysis_overview.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print("Visualizations saved to results/visualizations/")
    
    def generate_report(self):
        """Generate analysis report"""
        print("Generating report...")
        
        report = []
        report.append("CORD-19 Dataset Analysis Report")
        report.append("=" * 40)
        report.append("")
        
        # Basic stats
        report.append("Dataset Overview:")
        report.append(f"- Total records: {len(self.df):,}")
        
        if 'year' in self.df.columns:
            year_counts = self.df['year'].value_counts().sort_index()
            peak_year = year_counts.idxmax()
            report.append(f"- Year range: {self.df['year'].min():.0f} - {self.df['year'].max():.0f}")
            report.append(f"- Peak year: {peak_year} ({year_counts.max():,} papers)")
        
        if 'journal' in self.df.columns:
            top_journal = self.df['journal'].value_counts().index[0]
            top_count = self.df['journal'].value_counts().iloc[0]
            report.append(f"- Top journal: {top_journal} ({top_count:,} papers)")
            report.append(f"- Unique journals: {self.df['journal'].nunique():,}")
        
        if 'title_length' in self.df.columns:
            avg_title = self.df['title_length'].mean()
            report.append(f"- Average title length: {avg_title:.1f} characters")
        
        if 'abstract_length' in self.df.columns:
            avg_abstract = self.df['abstract_length'].mean()
            report.append(f"- Average abstract length: {avg_abstract:.1f} characters")
        
        report.append("")
        report.append("Key Insights:")
        
        if 'year' in self.df.columns and peak_year >= 2020:
            report.append("- COVID-19 pandemic led to surge in research publications")
        
        if 'journal' in self.df.columns:
            concentration = self.df['journal'].value_counts().head(10).sum() / len(self.df) * 100
            report.append(f"- Top 10 journals publish {concentration:.1f}% of all papers")
        
        # Save report
        report_text = "\n".join(report)
        with open("results/analysis_report.txt", "w") as f:
            f.write(report_text)
        
        print(report_text)
        print("\nReport saved to results/analysis_report.txt")
    
    def run_analysis(self):
        """Run complete analysis"""
        print("Starting CORD-19 Analysis")
        print("-" * 30)
        
        if not self.load_data():
            return False
        
        self.clean_data()
        self.create_visualizations()
        self.generate_report()
        
        print("\nAnalysis complete!")
        print("Files created:")
        print("- results/analysis_report.txt")
        print("- results/visualizations/publication_trends.png")
        print("- results/visualizations/top_journals.png")
        print("- results/visualizations/text_analysis_overview.png")
        
        return True

def main():
    analyzer = SimpleAnalyzer()
    analyzer.run_analysis()

if __name__ == "__main__":
    main()