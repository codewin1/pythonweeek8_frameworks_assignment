"""
CORD-19 Analysis Dashboard
Simple version with clean interface and minimal code
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os
from pathlib import Path

st.set_page_config(page_title="CORD-19 Analysis", layout="wide")

def load_analysis_results():
    """Load pre-generated results from analysis.py"""
    results = {}
    
    # Check for report
    report_path = Path("results/analysis_report.txt")
    results['has_report'] = report_path.exists()
    if results['has_report']:
        results['report'] = report_path.read_text()
    
    # Check for visualizations
    viz_dir = Path("results/visualizations")
    results['visualizations'] = {}
    if viz_dir.exists():
        for viz_file in ['publication_trends.png', 'top_journals.png', 'text_analysis_overview.png']:
            results['visualizations'][viz_file] = (viz_dir / viz_file).exists()
    
    return results

@st.cache_data
def load_data(uploaded_file, sample_size=None):
    """Load CSV data"""
    try:
        if sample_size:
            return pd.read_csv(uploaded_file, nrows=sample_size)
        return pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

def preprocess_data(df):
    """Basic data preprocessing"""
    df = df.copy()
    
    if 'publish_time' in df.columns:
        df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
        df['year'] = df['publish_time'].dt.year
        # Filter reasonable years
        df = df[(df['year'] >= 1990) & (df['year'] <= 2024) | df['year'].isna()]
    
    if 'title' in df.columns:
        df['title_length'] = df['title'].fillna('').str.len()
    
    if 'abstract' in df.columns:
        df['abstract_length'] = df['abstract'].fillna('').str.len()
    
    return df

def create_publication_chart(df):
    """Create publication trends chart"""
    if 'year' not in df.columns:
        return None
    
    year_counts = df['year'].dropna().value_counts().sort_index()
    if len(year_counts) == 0:
        return None
    
    fig = px.line(x=year_counts.index, y=year_counts.values,
                  title="Publications by Year",
                  labels={'x': 'Year', 'y': 'Publications'})
    return fig

def create_journal_chart(df, top_n=10):
    """Create top journals chart"""
    if 'journal' not in df.columns:
        return None
    
    journal_counts = df['journal'].value_counts().head(top_n)
    if len(journal_counts) == 0:
        return None
    
    fig = px.bar(x=journal_counts.values, y=journal_counts.index,
                 orientation='h', title=f"Top {top_n} Journals",
                 labels={'x': 'Publications', 'y': 'Journal'})
    fig.update_layout(height=500)
    return fig

def main():
    st.title("CORD-19 Dataset Analysis")
    st.write("Analysis dashboard for COVID-19 research publications")
    
    # Load pre-generated results
    results = load_analysis_results()
    
    # Tabs for different views
    tab1, tab2 = st.tabs(["Pre-Generated Results", "Live Analysis"])
    
    with tab1:
        st.header("Results from analysis.py")
        
        if results['has_report']:
            st.success("Analysis results available")
            
            # Show visualizations
            viz_dir = Path("results/visualizations")
            for viz_name, available in results['visualizations'].items():
                if available:
                    viz_path = viz_dir / viz_name
                    st.subheader(viz_name.replace('_', ' ').replace('.png', '').title())
                    st.image(str(viz_path))
            
            # Show report in expandable section
            with st.expander("View Analysis Report"):
                st.text(results['report'])
        else:
            st.warning("No pre-generated results found. Run 'python analysis.py' first.")
    
    with tab2:
        st.header("Interactive Analysis")
        
        uploaded_file = st.file_uploader("Upload metadata.csv", type=['csv'])
        
        if uploaded_file:
            # Sample size control
            sample_size = st.slider("Sample size", 1000, 20000, 10000, 1000)
            
            # Load and process data
            df = load_data(uploaded_file, sample_size)
            if df is not None:
                df = preprocess_data(df)
                
                st.success(f"Loaded {len(df):,} records")
                
                # Basic metrics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Papers", f"{len(df):,}")
                with col2:
                    if 'year' in df.columns:
                        year_range = f"{df['year'].min():.0f} - {df['year'].max():.0f}"
                        st.metric("Year Range", year_range)
                with col3:
                    if 'journal' in df.columns:
                        st.metric("Unique Journals", df['journal'].nunique())
                
                # Charts
                pub_chart = create_publication_chart(df)
                if pub_chart:
                    st.plotly_chart(pub_chart, use_container_width=True)
                
                journal_chart = create_journal_chart(df)
                if journal_chart:
                    st.plotly_chart(journal_chart, use_container_width=True)
                
                # Data preview
                st.subheader("Data Preview")
                preview_cols = ['title', 'journal', 'year'] if 'title' in df.columns else df.columns[:3]
                st.dataframe(df[preview_cols].head(20))

if __name__ == "__main__":
    main()