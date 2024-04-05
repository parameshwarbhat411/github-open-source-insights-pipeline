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
