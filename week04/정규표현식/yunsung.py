# Matching Same Text Again & Again
Regex_Pattern = r'([a-z]\w\s\W\d\D[A-Z][a-zA-Z][aeiouAEIOU]\S)\1'

# Branch Reset Groups
Regex_Pattern = '/^\d{2}(?|(:)|(.)|(---)|(-))\d{2}\1\d{2}\1\d{2}$/'

# Forward References
Regex_Pattern = '/^(\2tic|(tac))*$/'

# Positive Lookahead
Regex_Pattern = r'o(?=oo)'

# Negative Lookahead
Regex_Pattern = r"(.)(?!\1)"

# Positive Lookbehind
Regex_Pattern = r"(?<=[13579])\d"

# Negative Lookbehind
Regex_Pattern = r"(?<![aeiuoAEIOU])."