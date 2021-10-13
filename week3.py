# 없는 숫자 더하기

def solution(numbers):
    
    return 45-sum(numbers)

import re

# Excluding Specific Characters

Regex_Pattern = r'^\D[^aeiou][^bcDF]\S[^AEIOU][^.,]$'	# Do not delete 'r'.

# Matching Word Boundaries

Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'	# Do not delete 'r'.