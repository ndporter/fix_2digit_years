#2023-01-24
#Nathaniel D. Porter
#CC-0 (public domain, reuse and remix freely)

def fix_2digit_years(stringdate,century='19',separator='/',yearpos=-1):
    """
    Args:
      stringdate: A date in string format which may use 2-digit year conventions.
      century: A 2-digit string to prepend to 2-digit years when found (defaults to `19`). Does not currently support data spanning multiple centuries.
      separator: A string specifying the character used to separate sections of the date (defaults to `/`). Will not work for dates without separators (i.e. 20220111).
      yearpos: The position of the year in the year, month, day series (defaults to final).
    
    Returns:
      A copy of the string or (if the original string had a 2-digit year) a copy of the string converted to a 4-digit year.
    """
    chunks = stringdate.split(sep=separator)
    if len(chunks[yearpos]) == 2:
        chunks[yearpos] = century+chunks[yearpos]
    return separator.join(chunks)
