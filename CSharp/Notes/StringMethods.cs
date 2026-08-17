using System;

namespace CSharpLearning.Topics
{
    class StringMethods
    {
        public static void Run()
        {
            string fullName = "Bro Code";       // note: 'string' (lowercase) is preferred over 'String'
            string phoneNumber = "123-456-7890"; // both work, lowercase is the C# convention

            // ─────────────────────────────────────────
            // IMPORTANT RULE: strings are IMMUTABLE in C#
            // That means string methods do NOT change the original string
            // They return a NEW string — you must reassign to keep the result
            // ─────────────────────────────────────────

            // ─────────────────────────────────────────
            // 1. CASE CONVERSION
            // ─────────────────────────────────────────

            string upper = fullName.ToUpper();   // "BRO CODE" — original unchanged
            string lower = fullName.ToLower();   // "bro code"
            Console.WriteLine(upper);
            Console.WriteLine(lower);

            // ─────────────────────────────────────────
            // 2. REPLACE
            // ─────────────────────────────────────────

            // Replace(oldValue, newValue) — swaps every occurrence of oldValue with newValue
            phoneNumber = phoneNumber.Replace("-", "");       // "1234567890" — removes all dashes
            string hyphenated = "hello world".Replace(" ", "-"); // "hello-world"
            Console.WriteLine(phoneNumber);

            // ─────────────────────────────────────────
            // 3. INSERT
            // ─────────────────────────────────────────

            // Insert(index, value) — inserts a string at the given position
            // index 0 = beginning of string
            string userName = fullName.Insert(0, "Mr. ");    // "Mr. Bro Code"
            string withComma = fullName.Insert(3, ",");      // "Bro, Code"
            Console.WriteLine(userName);

            // ─────────────────────────────────────────
            // 4. LENGTH
            // ─────────────────────────────────────────

            // .Length → total number of characters including spaces
            Console.WriteLine(fullName.Length);   // "Bro Code" → 8 (space counts!)

            // ─────────────────────────────────────────
            // 5. SUBSTRING
            // ─────────────────────────────────────────

            // Substring(startIndex, length) — extracts a portion of the string
            // startIndex → where to start (0-based, just like arrays)
            // length     → how many characters to take

            // "Bro Code"
            //  0123456 7  ← index positions

            string firstName = fullName.Substring(0, 3);   // start at 0, take 3 → "Bro"
            string lastName = fullName.Substring(4, 4);   // start at 4, take 4 → "Code"
            Console.WriteLine(firstName);
            Console.WriteLine(lastName);

            // Substring(startIndex) with ONE argument → takes everything from that index to end
            string fromIndex4 = fullName.Substring(4);     // "Code"

            // ─────────────────────────────────────────
            // 6. TRIM — REMOVING WHITESPACE
            // ─────────────────────────────────────────

            string messy = "   hello world   ";
            string trimmed = messy.Trim();        // "hello world"  — removes both sides
            string trimmedLeft = messy.TrimStart();   // "hello world   " — removes left only
            string trimmedRight = messy.TrimEnd();     // "   hello world" — removes right only

            // Very useful when cleaning up user input from Console.ReadLine()

            // ─────────────────────────────────────────
            // 7. CONTAINS, STARTSWITH, ENDSWITH
            // ─────────────────────────────────────────

            string sentence = "The quick brown fox";

            bool hasWord = sentence.Contains("quick");      // true  — checks anywhere in string
            bool starts = sentence.StartsWith("The");      // true  — checks beginning
            bool ends = sentence.EndsWith("fox");        // true  — checks end
            bool notThere = sentence.Contains("cat");        // false

            Console.WriteLine(hasWord);   // True
            Console.WriteLine(starts);    // True
            Console.WriteLine(ends);      // True

            // ─────────────────────────────────────────
            // 8. INDEXOF — FINDING A CHARACTER OR WORD
            // ─────────────────────────────────────────

            // IndexOf() → returns the INDEX of the first match, or -1 if not found
            string email = "ujjwal@gmail.com";
            int atPosition = email.IndexOf("@");     // 6
            int dotPosition = email.IndexOf(".");    // 13
            int notFound = email.IndexOf("z");       // -1

            Console.WriteLine(atPosition);   // 6
            Console.WriteLine(notFound);     // -1

            // Common pattern: check if something exists before using it
            if (email.IndexOf("@") != -1)
                Console.WriteLine("Valid email format");

            // ─────────────────────────────────────────
            // 9. SPLIT — BREAKING A STRING INTO PARTS
            // ─────────────────────────────────────────

            // Split(separator) → breaks string into an array of substrings
            string csv = "apple,banana,mango,grape";
            string[] fruits = csv.Split(',');    // ["apple", "banana", "mango", "grape"]

            foreach (string fruit in fruits)
                Console.WriteLine(fruit);

            string sentence2 = "Hello World How Are You";
            string[] words = sentence2.Split(' ');   // splits on space → each word becomes an element

            // ─────────────────────────────────────────
            // 10. STRING.JOIN — OPPOSITE OF SPLIT
            // ─────────────────────────────────────────

            // Joins an array back into a single string with a separator
            string joined = string.Join(", ", fruits);   // "apple, banana, mango, grape"
            string joinedDash = string.Join("-", fruits); // "apple-banana-mango-grape"
            Console.WriteLine(joined);

            // ─────────────────────────────────────────
            // 11. REMOVE
            // ─────────────────────────────────────────

            // Remove(startIndex, count) → removes characters from the string
            string word = "Hello!!!";
            string cleaned = word.Remove(5, 3);   // start at index 5, remove 3 chars → "Hello"

            // Remove(startIndex) with ONE argument → removes everything from that index to end
            string trimEnd = word.Remove(5);      // "Hello"

            // ─────────────────────────────────────────
            // 12. STRING.IsNullOrEmpty / IsNullOrWhiteSpace
            // ─────────────────────────────────────────

            // Checks if a string is null, empty, or just whitespace
            // Very important for validating user input

            string input1 = "";
            string input2 = "   ";
            string input3 = null;
            string input4 = "hello";

            Console.WriteLine(string.IsNullOrEmpty(input1));          // True  — empty
            Console.WriteLine(string.IsNullOrEmpty(input2));          // False — has spaces
            Console.WriteLine(string.IsNullOrWhiteSpace(input2));     // True  — only whitespace
            Console.WriteLine(string.IsNullOrWhiteSpace(input3));     // True  — null
            Console.WriteLine(string.IsNullOrEmpty(input4));          // False — has content

            // ─────────────────────────────────────────
            // 13. EQUALS & COMPARISON
            // ─────────────────────────────────────────

            string a = "hello";
            string b = "HELLO";

            bool exactMatch = a.Equals(b);   // false — case sensitive by default

            // Case-insensitive comparison (most useful in real apps)
            bool caseInsensitive = a.Equals(b, StringComparison.OrdinalIgnoreCase);  // true
            Console.WriteLine(caseInsensitive);  // True

            // For user input comparisons, always use OrdinalIgnoreCase
            // so "YES", "yes", "Yes" all match

            // ─────────────────────────────────────────
            // 14. QUICK REFERENCE
            // ─────────────────────────────────────────
            // .ToUpper()                          → all uppercase
            // .ToLower()                          → all lowercase
            // .Replace(old, new)                  → swap characters/words
            // .Insert(index, value)               → insert at position
            // .Length                             → character count (spaces included)
            // .Substring(start, length)           → extract portion
            // .Substring(start)                   → extract to end
            // .Trim() / TrimStart() / TrimEnd()   → remove whitespace
            // .Contains(value)                    → true/false if found
            // .StartsWith(value)                  → true/false
            // .EndsWith(value)                    → true/false
            // .IndexOf(value)                     → position, or -1 if not found
            // .Split(separator)                   → string → array
            // string.Join(separator, array)       → array → string
            // .Remove(start, count)               → delete characters
            // string.IsNullOrEmpty(s)             → checks null or ""
            // string.IsNullOrWhiteSpace(s)        → checks null, "", or "   "
            // .Equals(s, StringComparison.OrdinalIgnoreCase) → case-insensitive compare

            Console.ReadKey();
        }
    }
}