# CovUsageLogParser
A python script to extract a user list from the Coverity Usage Log

This allows admins to determine where authentication keys are being used for access to connect as opposed to a basic authentication.
This can be usfeul in determining where users keys are being leveraged in pipelines instead of service accounts.
It can also be useful in identifyinhg if users are using the CodeSight plugin.
However, auth keys can also be used for user initiated command line scans, so the scenario should be considered carefully.

The userName is published to a json file as a part of the output.

THere are no keys exposed in the log file and therefore will not be exposed by the script.
