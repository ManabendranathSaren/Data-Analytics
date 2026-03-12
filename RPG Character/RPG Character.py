full_dot = '●'
empty_dot = '○'

def create_character(NAME, STRE, INTE, CHAR):
    if not isinstance(NAME, str):
        return 'The character name should be a string'
    if not isinstance(NAME, ""):
        return 'The character should have a name'
    if len(NAME) > 10:
        return 'The character name is too long'
    if x in NAME == " ":
        return 'The character name should not contain spaces'
    if not isinstance(STRE, INTE):
        return 'All stats should be integers'
    if not isinstance(INTE, INTE):
        return 'All stats should be integers'
    if not isinstance(CHAR, INTE):
        return 'All stats should be integers'
    if STRE < 1 or CHAR < 1 or INTE < 1 :
        return 'All stats should be no less than 1'
    if STRE > 4 or CHAR > 4 or INTE > 4 :
        return 'All stats should be no more than 4'
    if (STRE + INTE + CHAR) != 7 :
        return "The character should start with 7 points"
    
    
    print("NAME ", NAME)
    print("STRE ", STRE)
    print("INTE ", INTE)
    print("CHAR ", CHAR)
