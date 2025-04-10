import streamlit as st
from streamlit import query_params as qp
import aiohttp
import asyncio
import re
import time
import requests
import json
from datetime import datetime, timedelta

st.info("Share Booster by Kein Villareal")

# Define the URL to the owner's Facebook page
owner_facebook_url = "https://www.facebook.com/profile.php?id=61571644877640"  # Replace with the actual URL

# Password setup

password = "free1999"  # Replace 'premium' with the actual password
password_set_time = datetime.now()  # Record the time when the password is set

# Function to check if the password has expired
def has_password_expired(set_time, years=99, months=12, days=31, hours=24):
    # Calculate expiration time based on years, months, days, and hours
    expiration_time = set_time + timedelta(days=days + months * 30 + years * 365, hours=hours)
    return datetime.now() > expiration_time

# Password prompt
password_prompt = st.text_input("Enter the Access Key", type='password')
st.markdown(f"[Avail to the Owner]({owner_facebook_url})")  # Link to the owner's Facebook page

# Check for the correct password
if password_prompt == password and not has_password_expired(password_set_time, years=40, months=12, days=1, hours=24):

    def Execute(cookie, post, share_count, delay):
        head = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
