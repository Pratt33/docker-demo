import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Page configuration
st.set_page_config(
    page_title="Amazon Web Scraper",
    layout="wide"
)

# Title
st.title("Amazon Product Scraper")
st.markdown("A simple tool to scrape product information from Amazon")

# Sidebar
st.sidebar.header("Configuration")
max_products = st.sidebar.slider("Max products to scrape", 1, 20, 5)

# Main content
product_url = st.text_input(
    "Enter Amazon Product URL:",
    placeholder="https://www.amazon.com/..."
)

if st.button("Scrape Product Info"):
    if product_url:
        with st.spinner("Scraping product information..."):
            try:
                # Basic headers to avoid blocking
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                
                response = requests.get(product_url, headers=headers)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Try to extract basic product info (this is a simplified version)
                title_element = soup.find('span', {'id': 'productTitle'})
                price_element = soup.find('span', {'class': 'a-price-whole'})
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Product Information")
                    if title_element:
                        st.write("**Title:**", title_element.get_text().strip())
                    else:
                        st.write("**Title:** Not found")
                    
                    if price_element:
                        st.write("**Price:** $", price_element.get_text().strip())
                    else:
                        st.write("**Price:** Not found")
                
                with col2:
                    st.subheader("Raw Data")
                    st.write("**Response Status:**", response.status_code)
                    st.write("**URL:**", product_url)
                
                # Display some raw HTML for testing
                with st.expander("View Raw HTML (first 1000 chars)"):
                    st.code(str(soup)[:1000])
                    
            except Exception as e:
                st.error(f"Error scraping product: {str(e)}")
    else:
        st.warning("Please enter a product URL")

# Sample data section
st.markdown("---")
st.subheader("Sample Data")

# Create sample data
sample_data = {
    'Product': ['iPhone 14', 'Samsung Galaxy S23', 'Google Pixel 7'],
    'Price': ['$999', '$899', '$699'],
    'Rating': [4.5, 4.3, 4.2],
    'Reviews': [1523, 892, 674]
}

df = pd.DataFrame(sample_data)
st.dataframe(df, use_container_width=True)

# Footer
st.markdown("---")