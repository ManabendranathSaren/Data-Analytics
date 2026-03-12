full_dot = '●'
empty_dot = '○'

def create_character(NAME, STRE, INTE, CHAR):
    if not isinstance(NAME, str):
        return 'The character name should be a string'
    if len(NAME) == 0:
        return 'The character should have a name'
    if " " in NAME:
        return 'The character name should not contain spaces'
    if len(NAME) > 10:
        return 'The character name is too long'
    if not isinstance(STRE, int):
        return 'All stats should be integers'
    if not isinstance(INTE, int):
        return 'All stats should be integers'
    if not isinstance(CHAR, int):
        return 'All stats should be integers'
    if STRE < 1 or CHAR < 1 or INTE < 1 :
        return 'All stats should be no less than 1'
    if STRE > 4 or CHAR > 4 or INTE > 4 :
        return 'All stats should be no more than 4'
    if (STRE + INTE + CHAR) != 7 :
        return "The character should start with 7 points"
    
    STRE = STRE*full_dot + (10-STRE)*empty_dot
    INTE = INTE*full_dot + (10-INTE)*empty_dot
    CHAR = CHAR*full_dot + (10-CHAR)*empty_dot
    print("NAME ", NAME)
    print("STRE ", STRE)
    print("INTE ", INTE)
    print("CHAR ", CHAR)

create_character("Manab",4,2,1)
    
    print("NAME ", NAME)
    print("STRE ", STRE)
    print("INTE ", INTE)
    print("CHAR ", CHAR)


# Output
'''
NAME  Manab
STRE  ●●●●○○○○○○
INTE  ●●○○○○○○○○
CHAR  ●○○○○○○○○○
'''
