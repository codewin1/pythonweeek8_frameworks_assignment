# CORD-19 Dataset Analysis Project

## Project Overview

This project demonstrates a complete data science workflow using the CORD-19 research dataset. It includes comprehensive analysis of COVID-19 research publications, interactive visualizations, and a web application for data exploration.

### Assignment Context
**Course**: Frameworks Assignment  
**Topic**: CORD-19 Research Dataset Analysis  
**Objective**: Demonstrate data science workflow from data loading to insights generation  
**Technologies**: Python, Pandas, Matplotlib, Seaborn, Streamlit, Plotly  

## Features

### Analysis Script (`analysis.py`)
- **Data Loading & Validation**: Robust CSV processing with error handling
- **Data Cleaning**: Handles missing values, invalid dates, and text preprocessing  
- **Publication Trends**: Time-series analysis of research output
- **Journal Analysis**: Identification of top publishers and concentration metrics
- **Text Analytics**: Title/abstract length analysis and completeness assessment
- **Automated Visualizations**: Publication trends, journal rankings, text distributions
- **Comprehensive Reporting**: Automated insights generation and summary reports

### Interactive Dashboard (`streamlit_app.py`)
- **File Upload Interface**: Easy CSV upload with sample size controls
- **Real-time Processing**: Dynamic data preprocessing and analysis
- **Interactive Charts**: Publication trends with peak year annotations
- **Journal Explorer**: Top publishers with filterable rankings  
- **Text Analysis**: Length distributions and completeness metrics
- **Keyword Analysis**: Most frequent terms extraction and visualization
- **Data Explorer**: Filterable data browser with export capabilities
- **Responsive Design**: Modern UI with custom styling and insights panels

##  Project Structure

```
frameworks_assignment/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── analysis.py                  # Main analysis script
├── streamlit_app.py            # Interactive web application
├── data/                       # Dataset directory
│   └── metadata.csv            # CORD-19 metadata file
├── results/                    # Analysis outputs (auto-generated)
│   ├── analysis_report.txt     # Comprehensive text report
│   └── visualizations/         # Generated plots
│       ├── publication_trends.png
│       ├── top_journals.png
│       └── text_analysis_overview.png
└── .gitignore                  # Git ignore file
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### 1. Clone Repository 
```bash 
git clone https://github.com/codewin1/pythonweeek8_frameworks_assignment
 ```
Change the directory
 ```
cd Downloads/frameworks_assignment
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download Dataset
1. Visit [Kaggle CORD-19 Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
2. Download `metadata.csv`
3. Place in the `data/` folder

### 4. Verify Installation
```bash
python -c "import pandas, matplotlib, streamlit; print('All dependencies installed!')"
```

## Usage Guide

### Option 1: Run Complete Analysis Script
```bash
python analysis.py
```

**What it does:**

- Loads and explores the dataset
- Performs comprehensive cleaning and preprocessing
- Analyzes publication trends and journal patterns  
- Generates text analytics and insights
- Creates and saves all visualizations
- Produces a detailed analysis report

**Output:**
- Text report: `results/analysis_report.txt`
- Visualizations: `results/visualizations/*.png`
- Console output with key findings

### Option 2: Launch Interactive Dashboard  
```bash
streamlit run streamlit_app.py
```

**What it provides:**
- Web interface at `http://localhost:8501`
- Interactive file upload and processing
- Real-time chart generation and filtering
- Keyword analysis and data exploration
- Export capabilities for filtered data

**Usage:**
1. Open web browser to localhost:8501
2. Upload your `metadata.csv` file via sidebar
3. Adjust sample size for performance (recommended: 15,000)
4. Explore different analysis tabs
5. Use filters in Data Explorer for specific insights

## 📊 Analysis Results

### Key Findings (Sample Dataset)

#### Publication Trends
- **Peak Research Year**: 2020-2021 (COVID-19 pandemic surge)
- **Research Growth**: 10x increase during pandemic years
- **Publication Pattern**: Consistent growth with pandemic spike

#### Journal Analysis  
- **Total Journals**: 3,000+ unique publications
- **Top Publisher**: [Varies by dataset sample]
- **Concentration**: Top 10 journals publish ~30% of papers
- **Distribution**: Long tail with many single-publication journals

#### Text Characteristics
- **Average Title Length**: ~80 characters
- **Average Abstract Length**: ~1,200 characters  
- **Content Ratio**: Abstracts 15x longer than titles
- **Data Completeness**: 85%+ papers include abstracts

### Generated Visualizations

1. **Publication Trends Over Time**
   - Line chart showing research output by year
   - Peak year annotation and trend analysis
   - Clear COVID-19 research surge visualization

2. **Top Journals Rankings** 
   - Horizontal bar chart of leading publishers
   - Publication counts and market share
   - Color-coded frequency visualization

3. **Text Analysis Overview**
   - Multi-panel visualization including:
   - Title/abstract length distributions
   - Monthly publication patterns  
   - Data completeness pie chart

## 🔍 Data Science Workflow Demonstrated

### 1. Data Loading & Validation
- File existence checking and error handling
- Memory usage optimization with sampling options
- Column validation and type checking

### 2. Exploratory Data Analysis  
- Missing data assessment and quantification
- Data type analysis and structure exploration
- Initial statistical summaries and insights

### 3. Data Cleaning & Preprocessing
- Date parsing and validation (1990-2024 range)
- Text metric calculation (title/abstract lengths)
- Data quality filtering and completeness assessment
- Removal of invalid records with detailed logging

### 4. Statistical Analysis
- Time-series trend analysis with peak detection
- Journal concentration and market share analysis
- Text characteristics and content quality metrics
- Data completeness and quality assessment

### 5. Visualization & Communication

- Automated chart generation with consistent styling
- Interactive web dashboards with real-time filtering
- Professional report generation with key insights
- Export capabilities for further analysis

## Technical Highlights

### Performance Optimization

- **Caching**: Streamlit data caching for improved performance
- **Sampling**: Configurable dataset sampling for large files
- **Memory Management**: Efficient pandas operations and cleanup

### User Experience

- **Error Handling**: Comprehensive error messages and fallbacks
- **Progress Indicators**: Loading spinners and status updates  
- **Responsive Design**: Mobile-friendly layouts and interactions
- **Export Options**: CSV download and report generation

### Code Quality

- **Documentation**: Comprehensive docstrings and comments
- **Modularity**: Clean class-based architecture  
- **Reusability**: Configurable parameters and flexible inputs
- **Best Practices**: PEP8 compliance and error handling

## Learning Outcomes Achieved

**Python Data Analysis Skills**

- Pandas for data manipulation and cleaning
- NumPy for numerical computations
- Advanced data preprocessing techniques

**Visualization Proficiency**  

- Matplotlib for static publication-quality plots
- Plotly for interactive web-based visualizations
- Seaborn for statistical visualization aesthetics

**Web Application Development**

- Streamlit framework for rapid prototyping
- Interactive dashboard design principles
- User experience and interface optimization

**Data Science Workflow**

- End-to-end project structure and organization
- Automated analysis pipeline development
- Professional reporting and insight generation

**Real-world Dataset Experience**

- Large-scale scientific dataset handling
- Data quality assessment and improvement
- Domain-specific analysis and interpretation

### Potential Extensions

- **Machine Learning**: Topic modeling and classification
- **Network Analysis**: Author collaboration networks
- **Geographic Analysis**: Publication location mapping
- **Citation Analysis**: Impact and reference patterns
- **Time Series Forecasting**: Research trend prediction

### Technical Improvements  

- **Database Integration**: PostgreSQL or MongoDB storage
- **API Development**: REST API for data access
- **Advanced Filtering**: Complex query capabilities
- **Real-time Updates**: Automated dataset refresh
- **Performance Scaling**: Distributed computing support

## Dependencies

```text
pandas>=1.3.0          # Data manipulation and analysis
matplotlib>=3.5.0       # Static plotting and visualization  
seaborn>=0.11.0        # Statistical data visualization
streamlit>=1.28.0      # Web application framework
plotly>=5.15.0         # Interactive plotting library
numpy>=1.21.0          # Numerical computing fundamentals
```

## Contributing

This project is part of an academic assignment. For educational purposes:

1. Fork the repository
2. Experiment with different analysis approaches
3. Try alternative visualization techniques  
4. Implement additional features from the enhancement list
5. Share insights and improvements
