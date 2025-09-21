#!/bin/bash

echo "Running analysis.py..."
python3 analysis.py

if [ $? -eq 0 ]; then
    echo "Analysis succeeded. Starting Streamlit app..."
    streamlit run streamlit_app.py
else
    echo "Analysis failed. Skipping the web app."
fi
