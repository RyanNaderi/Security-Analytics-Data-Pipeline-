# Security Analytics Data Pipeline

A Python-based security analytics pipeline designed to analyze authentication logs and identify suspicious login behavior. The project simulates a simplified Security Operations Center (SOC) workflow by processing raw login data, storing it in a SQLite database, applying SQL-based analysis, and generating security reports.

## Project Overview

The pipeline performs the following steps:

1. Loads authentication logs from CSV files
2. Stores structured log data in a SQLite database
3. Uses SQL queries to analyze failed login attempts and user activity
4. Applies time-window analysis to detect bursts of failed authentication attempts
5. Classifies activity based on risk thresholds
6. Generates reports summarizing suspicious login behavior

## Technologies Used

* Python
* Pandas
* SQLite
* SQL
* Matplotlib
* CSV

## Detection Logic

Users are flagged as suspicious when they exceed a defined threshold of failed login attempts within a specified time window. The generated reports include affected users, failure counts, detection windows, and the reason for the alert.
