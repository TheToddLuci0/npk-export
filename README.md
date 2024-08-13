# NPK Export

Export all the cracked hashes from your NPK instance. Automatically dedupes to
reduce filesize. RAM requirements scale based on number of hashes to parse.

Useful for:
- Generating wordlists
- Computing statistics across campaigns
- Circumventing the built-in retention policies

# WARNING
Seriously, don't do this unless you've got a good reason, and are willing to 
take on the risk of putting all these hashes in one place. In-the-wild crack
jobs often contain client identifiable information (Looking at you, 
`Examplecorp2024`). 


## Useage
`AWS_PROFILE=npk python3 export.py > potfile`

