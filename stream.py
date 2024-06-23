import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Function to fetch latest repos from the backend
def fetch_latest_repos():
    response = requests.get('http://127.0.0.1:5000/latest_repos')
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Function to fetch repo data for visualizations
def fetch_repo_data(repo_id):
    response = requests.get(f'http://127.0.0.1:5000/repo_data?repo_id={repo_id}')
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Streamlit app
st.title('GitHub Repository Viewer')

# Fetch the latest repos
latest_repos = fetch_latest_repos()

# Convert the repos to a DataFrame for easy manipulation
df_repos = pd.DataFrame(latest_repos)

# Display the selectbox for repository names
repo_name = st.selectbox(
    'Select a GitHub Repo:',
    df_repos['repo_name'] if not df_repos.empty else []
)

# Display a button to confirm selection
if st.button('Go to Dashboard'):
    # Fetch the selected repo_id
    repo_id = df_repos[df_repos['repo_name'] == repo_name]['repo_id'].values[0]

    # Fetch data for the selected repo
    repo_data = fetch_repo_data(repo_id)
    df_repo_data = pd.DataFrame(repo_data, columns=['date_month', 'repo_id', 'star_count', 'last_year_star_count', 'yoy_growth'])
    df_repo_data['date_month'] = pd.to_datetime(df_repo_data['date_month'], format='%a, %d %b %Y %H:%M:%S %Z',
                                                errors='coerce')
    # Plot: Monthly Star Count Over Time
    st.header(f'Growth Over Time for {repo_name}')
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_repo_data, x='date_month', y='star_count')
    plt.title('Monthly Star Count Over Time')
    plt.xlabel('Date')
    plt.ylabel('Star Count')
    st.pyplot(plt)

    # Plot: Year-on-Year Growth Over Time
    st.header(f'Year-on-Year Growth for {repo_name}')
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_repo_data, x='date_month', y='yoy_growth')
    plt.title('Year-on-Year Growth Over Time')
    plt.xlabel('Date')
    plt.ylabel('Year-on-Year Growth')
    st.pyplot(plt)

    # Plot: Cumulative Star Count Over Time
    df_repo_data['cumulative_stars'] = df_repo_data['star_count'].cumsum()
    st.header(f'Cumulative Star Count for {repo_name}')
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_repo_data, x='date_month', y='cumulative_stars')
    plt.title('Cumulative Star Count Over Time')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Star Count')
    st.pyplot(plt)

    st.header(f'Monthly Star Count Area Plot for {repo_name}')
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_repo_data, x='date_month', y='star_count')
    plt.fill_between(df_repo_data['date_month'], df_repo_data['star_count'], alpha=0.3)
    plt.title('Monthly Star Count Area Plot')
    plt.xlabel('Date')
    plt.ylabel('Star Count')
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(nbins=12))
    plt.gca().xaxis.set_major_formatter(
    plt.matplotlib.dates.DateFormatter('%Y-%m'))  # Format x-axis labels as Year-Month
    st.pyplot(plt)

    # Plot: Star Count Comparison
    st.header(f'Star Count Comparison for {repo_name}')
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_repo_data, x='date_month', y='star_count', label='Current Year')
    sns.lineplot(data=df_repo_data, x='date_month', y='last_year_star_count', label='Last Year')
    plt.title('Star Count Comparison')
    plt.xlabel('Date')
    plt.ylabel('Star Count')
    plt.legend()
    st.pyplot(plt)


