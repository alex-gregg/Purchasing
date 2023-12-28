import re
import os

issue_description = os.getenv('GITHUB_EVENT_ISSUE_BODY', '')
print(f'Issue Description: {issue_description}')

# Adjusted regular expression for ### Team
team_name_match = re.search(r'### Team\n([^\n]+)', issue_description)

if team_name_match and team_name_match.group(1):
    team_name = team_name_match.group(1).strip()
    print(f'Team Name: {team_name}')
    print(f'::set-output name=team-name::{team_name}')
else:
    print('::error::Team name not found in the issue description.')
