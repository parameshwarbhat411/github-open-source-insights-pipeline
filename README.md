# GitHub Gems: Driving Open-Source Investments With Data

Welcome to the GitHub Gems project! This project hosts a data analytics pipeline that enables smarter investment decisions by measuring the popularity of open-source repos on Github.

## Project Overview

The goal of this project is to develop an efficient data pipeline that streamlines analytics, reduces manual effort, and enables deeper insights into the open-source ecosystem on GitHub. By leveraging modern data tools and best practices, such as dbt (data build tool) and Airflow, we aim to create a scalable and reliable solution for data-driven decision-making.

## Getting Started

To get started with the GitHub Gems project, follow these steps (click on the
links for guides):

1. Set up your development environment by installing the necessary tools and dependencies. (VSCode, Python, PostgreSQL).

  a. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  b. [Install VSCode](https://www.postgresql.org/download/)
  c. [Install Python](https://www.python.org/downloads/)
  d. [Install PostgreSQL](https://www.postgresql.org/download/)

2. [Fork this repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) to your own GitHub account.

  a. Choose yourself as the owner.
  b. Modify the description to remove mentions of a template.

3. [Clone the forked
   repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository) to your local machine.

  a. You can use the HTTPS to clone your forked repo.


4. Create a python virtual environment for your repo

  a. Open a command line and cd into your repo folder.
  b. Run `python -m venv venv`
  c. Run `source venv/bin/activate`
  d. Make sure that your new virtual environment is activated.

5. Install python dependencies

  a. [Install dbt using pip](https://docs.getdbt.com/docs/core/pip-install).
  b. [Install Airflow using
  pip](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html)

6. Create a new branch to update this readme file and save your python
   dependencies.

7. Save your python dependencies by running `pip freeze > requirements.txt`

## Data Sampling Methodology

The data provided in the `/data` folder is a curated subset of the [GitHub Archive (GHA)](https://www.gharchive.org/) dataset, which records the public GitHub timeline. As the complete GHA dataset is approximately 17TB in size, it was necessary to sample the data to make it manageable for this project. However, it's important to note that this sampling approach introduces some caveats compared to working with the real-life GHA data, and our data ingestion process will differ slightly. The sampling process was as follows:

1. Seven representative repositories related to data engineering were selected as a starting point, including popular projects like Plotly. What else would you expect, given our love for data?

2. All events for these seven repositories were extracted from the GHA dataset, up until March 27, 2023. This resulted in a total of 244,066 events.

3. To reduce the size of the dataset, fields that are unnecessary for our analysis, such as repository URLs and user IDs, were removed.

4. The original GHA data is organized into hourly JSON files. To make the data more manageable, the events were aggregated into daily JSON files, resulting in a total of 3,840 files.

By using this curated dataset, we can dive into the data and perform meaningful analyses without the need for extensive data preprocessing or prohibitively large computational resources. However, it's crucial to keep in mind that this sampled dataset may not fully represent the entire GHA dataset, and certain insights or patterns unique to the complete dataset may not be discoverable in this subset.
