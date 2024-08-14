# Postmortem Report: The Great Website Meltdown of August 2024

![It’s Fine](https://github.com/Imane-Bjr/alx-system_engineering-devops/blob/master/assets/Fine.gif)

## Overview

On August 12, 2024, our main website experienced a significant outage, leaving users facing a frustrating 500 Internal Server Error. This README provides a detailed postmortem of the incident, including the timeline, root cause, resolution, and steps to prevent future occurrences.

## Incident Summary

- **Duration of Outage**: August 12, 2024, 10:00 AM - 12:30 PM UTC
- **Impact**: 100% of users encountered a 500 Internal Server Error when attempting to access the site.
- **Root Cause**: A missing WordPress configuration file (`wp-config.php`) caused PHP errors, leading Apache to fail.

## Timeline

- **10:00 AM UTC**: Users reported the site was down. Initial complaints started pouring in.
- **10:05 AM UTC**: Monitoring systems alerted the team to high error rates on Apache.
- **10:10 AM UTC**: Investigation began; Apache was found to be returning a 500 error.
- **10:20 AM UTC**: Strace was used to diagnose the problem, revealing issues with missing configuration files.
- **10:45 AM UTC**: Investigation initially focused on server resources and PHP settings, which were not the root cause.
- **11:00 AM UTC**: DevOps team was involved and identified the missing WordPress configuration file as the issue.
- **11:15 AM UTC**: The missing file was restored from backup, and Apache was restarted.
- **12:30 PM UTC**: The website was back online, and the incident was resolved.

## Root Cause and Resolution

- **Root Cause**: The `wp-config.php` file was missing, which caused PHP errors and led to Apache returning a 500 error.
- **Resolution**: Restored the missing file from backup and restarted Apache, resolving the issue.

## Corrective and Preventative Measures

To prevent similar incidents in the future, we will:

1. **Enhance Monitoring**: Implement alerts for missing critical files to catch issues before they impact users.
2. **Update Puppet Manifests**: Automate the deployment and verification of essential configuration files.
3. **Improve Documentation**: Document procedures for file recovery and configuration checks.
4. **Conduct Training**: Provide training on troubleshooting configuration issues and using diagnostic tools effectively.
5. **Verify Backups**: Regularly test backup integrity to ensure reliable recovery in case of future issues.

## Visual Aid

For a quick overview of the timeline, refer to the diagram below:

```plaintext
10:00 AM UTC - Website Down
  | 
10:05 AM UTC - Monitoring Alert
  |
10:10 AM UTC - Investigation Begins
  |
10:20 AM UTC - Strace Analysis
  |
10:45 AM UTC - Wild Goose Chase
  |
11:00 AM UTC - DevOps Involved
  |
11:15 AM UTC - File Restored
  |
12:30 PM UTC - Website Back Online

