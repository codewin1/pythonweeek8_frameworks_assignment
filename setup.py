import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    print("🐍 Checking Python version...")
    
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        print(f"   Current version: {sys.version}")
        return False
    else:
        print(f"✅ Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
        return True

def check_dependencies():
    """Check if required packages are installed."""
    print("\n📦 Checking dependencies...")
    
    required_packages = [
        ('pandas', 'Data manipulation'),
        ('numpy', 'Numerical computing'),
        ('matplotlib', 'Plotting'),
        ('seaborn', 'Statistical visualization'),
        ('plotly', 'Interactive charts'),
        ('streamlit', 'Web application framework')
    ]
    
    missing_packages = []
    
    for package, description in required_packages:
        try:
            __import__(package)
            print(f"✅ {package:<12} - {description}")
        except ImportError:
            print(f"❌ {package:<12} - {description} (MISSING)")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n💡 Install missing packages with:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False
    
    return True

def create_directory_structure():
    """Create necessary project directories."""
    print("\n📁 Creating directory structure...")
    
    directories = [
        'data',
        'results',
        'results/visualizations'
        'src/cord19_analysis.py'
        'src/streamlit_app.py'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {directory}/")
    
    return True

def check_data_file():
    """Check if the dataset file exists."""
    print("\n📊 Checking for dataset...")
    
    data_file = Path("data/metadata.csv")
    
    if data_file.exists():
        file_size = data_file.stat().st_size / (1024 * 1024)  # MB
        print(f"✅ Dataset found: {data_file} ({file_size:.1f} MB)")
        return True
    else:
        print(f"⚠️  Dataset not found: {data_file}")
        print("   💡 Download from: https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge")
        print("   📁 Place metadata.csv in the data/ folder")
        return False

def test_scripts():
    """Test if the main scripts can be imported."""
    print("\n🧪 Testing script imports...")
    
    scripts = [
        ('analysis.py', 'Main analysis script'),
        ('src/streamlit_app.py', 'Web dashboard')
    ]
    
    for script, description in scripts:
        if Path(script).exists():
            print(f"✅ {script:<20} - {description}")
        else:
            print(f"❌ {script:<20} - {description} (FILE MISSING)")
            return False
    
    return True

def display_usage_instructions():
    """Display usage instructions."""
    print("\n" + "="*60)
    print("🎉 SETUP COMPLETE!")
    print("="*60)
    
    print("\n🚀 Ready to run:")
    print("   1. Complete Analysis:")
    print("      python analysis.py")
    print("")
    print("   2. Interactive Dashboard:")
    print("      streamlit run streamlit_app.py")
    print("      Then open: http://localhost:8501")
    print("")
    
    print("📋 What each script does:")
    print("   • analysis.py      - Complete data analysis with saved results")
    print("   • streamlit_app.py - Interactive web dashboard for exploration")
    print("")
    
    print("📁 Project structure:")
    print("   • data/            - Place your metadata.csv here")  
    print("   • results/         - Analysis outputs and visualizations")
    print("   • README.md        - Complete documentation")

def main():
    """Main setup function."""
    print("🔬 CORD-19 Analysis Project Setup")
    print("=" * 40)
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies), 
        ("Directory Structure", create_directory_structure),
        ("Dataset", check_data_file),
        ("Scripts", test_scripts)
    ]
    
    all_passed = True
    
    for check_name, check_func in checks:
        try:
            if not check_func():
                all_passed = False
        except Exception as e:
            print(f"❌ Error during {check_name} check: {e}")
            all_passed = False
    
    if all_passed:
        display_usage_instructions()
    else:
        print("\n⚠️  Setup incomplete. Please resolve the issues above.")
        print("💡 Tip: Make sure you've run 'pip install -r requirements.txt'")

if __name__ == "__main__":
    main()