#JOBHawk AI Agent

🧑‍💻 User Story: JobHawk AI Job Tracker Agent
As a busy job-seeker,
I want an automated agent that checks job listings for specified roles across company career pages multiple times a day,
So that I can receive a regularly updated Excel-compatible file with relevant job openings that I can quickly review and apply to.



✅ Features (MVP)
Feature	Description
Scheduled Agent (4x/day)	Runs via AWS Lambda or a local cronjob to trigger the job-checking process.
Company List Lookup	Starts from a predefined list of companies or fetches them via an LLM using a seed role.
Career Page URL Finder	Uses an LLM to guess the company’s career page URL if not explicitly listed.
Job Scraper	Crawls the career page, filters Software Engineer (SWE) roles using fuzzy match or keyword match.
Data Store (SQLite)	Stores company name, job title, link, role match confidence, and timestamp. Avoids duplicate entries.
Output CSV (Excel-compatible)	Generates a clickable job list in .csv format and overwrites an existing file.
Notification System	Sends an email or push notification when new entries are added (optional, can use AWS SNS or SMTP).

📦 Phase-wise Breakdown
Phase 1: Company Career Page Agent
 Manually feed companies or ask LLM to find them.

 LLM finds career page URL.

 Store name and URL in DB.

Phase 2: Job Scraping & Storage
 Scrape jobs from career URLs.

 Filter by “Software Engineer”.

 Store new jobs in DB (no duplicates).

Phase 3: CSV Generation
 Convert SQLite data to .csv with clickable links.

 Save to ~/Downloads/JobHawk_<date>.csv.

Phase 4: Automation
 Schedule 4x daily run via:

Local cronjob for dev

AWS Lambda (with CloudWatch rule)

Phase 5: Notification (optional)
 Email or SMS using AWS SNS or SMTP.

 Only notify if new jobs were added.
