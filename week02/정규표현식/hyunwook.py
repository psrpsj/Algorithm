# Matching {x} Repetitions
Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'

# Matching {x, y} Repetitions
Regex_Pattern = r'^\w{1,2}[a-zA-Z]{3,}\W{,3}$'

# Matching Zero Or More Repetitions
Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$

# Matching One Or More Repetitions
Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'

# Matching Ending Items
Regex_Pattern = r'^[a-zA-Z]*s$'