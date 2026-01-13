# Password Strength Checker
## Scope
This project is currently CLI-based. If I decide to create a web version in the future, I’ll share the link here.

**No password storage**: The program does not store any passwords entered by users. It is purely for checking password strength.

**Open for everyone:** Anyone can use this tool to verify if their password is strong and resistant to common hacking techniques.

## What Defines a Strong Password?

**Length:** According to NIST guidelines, passwords should be 8 to 64 characters, with a recommendation of 15 or more characters (similar to a passphrase).

**Character Variety:** Use a mix of uppercase, lowercase, numbers, and special characters to increase complexity.

**Repetition:** Avoid repeated characters or patterns, as they make passwords easier to crack.

**Dictionary Words:** Passwords containing common dictionary words are considered weak.

**Wordlist Check:** Users can provide a custom wordlist file path. If none is provided, the program defaults to the popular rockyou.txt wordlist.
