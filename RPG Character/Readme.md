Tests:  
Passed:1. You should have a function named create_character.  
Passed:2. When create_character is called with a first argument that is not a string it should return The character name should be a string.  
Passed:3. When create_character is called with a first argument that is an empty string, it should return The character should have a name.  
Passed:4. When create_character is called with a first argument that is longer than 10 characters it should return The character name is too long.  
Passed:5. The create_character function should not say that the character is too long when it's not longer than 10 characters.  
Passed:6. When create_character is called with a first argument that contains a space it should return The character name should not contain spaces.  
Passed:7. When create_character is called with a second, third or fourth argument that is not an integer it should return All stats should be integers.  
Passed:8. When create_character is called with a second, third or fourth argument that is lower than 1 it should return All stats should be no less than 1.  
Passed:9. When create_character is called with a second, third or fourth argument that is higher than 4 it should return All stats should be no more than 4.  
Passed:10. When create_character is called with a second, third or fourth argument that do not sum to 7 it should return The character should start with 7 points.  
Failed:11. create_character('ren', 4, 2, 1) should return ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○.  
Failed:12. When create_character is called with valid values it should output the character stats as required.  
