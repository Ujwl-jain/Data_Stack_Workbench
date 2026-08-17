using System;

namespace CSharpLearning.Topics
{
    public class UserInput
    {
        public static void Run()
        {
            // ─────────────────────────────────────────
            // 1. BASIC USER INPUT
            // ─────────────────────────────────────────

            // Console.Write()   → prints text, cursor stays on SAME line (user types right after)
            // Console.WriteLine() → prints text, cursor moves to NEXT line

            Console.Write("Enter your name: ");   // cursor stays here → user types on same line
            string name = Console.ReadLine();      // ReadLine() reads everything the user types until they hit Enter
                                                   // always returns a string

            // ─────────────────────────────────────────
            // 2. READING NUMBERS — CONVERSION REQUIRED
            // ─────────────────────────────────────────

            // Console.ReadLine() ALWAYS gives back a string, even if the user types "25"
            // So you must convert it to the type you actually need

            Console.Write("Enter your age: ");
            int age = Convert.ToInt32(Console.ReadLine());   // string "25" → int 25

            // Other common conversions:
            double price = Convert.ToDouble(Console.ReadLine());   // string "9.99"  → double 9.99
            bool answer = Convert.ToBoolean(Console.ReadLine());   // string "true"  → bool true
            long bigNum = Convert.ToInt64(Console.ReadLine());     // string "99999" → long

            // Alternative: int.Parse() does the same thing as Convert.ToInt32()
            int age2 = int.Parse(Console.ReadLine());   // works the same
            // Difference: Convert.ToInt32(null) → returns 0 (safe)
            //             int.Parse(null)        → crashes with exception (unsafe)

            // ─────────────────────────────────────────
            // 3. SAFE CONVERSION WITH TryParse
            // ─────────────────────────────────────────

            // Problem: if user types "abc" instead of a number, Convert.ToInt32 will CRASH
            // Solution: int.TryParse() — tries to convert, returns true/false instead of crashing

            Console.Write("Enter a number: ");
            string input = Console.ReadLine();
            bool success = int.TryParse(input, out int parsedAge);  // 'out' keyword stores the result

            if (success)
            {
                Console.WriteLine($"Valid number: {parsedAge}");
            }
            else
            {
                Console.WriteLine("That was not a valid number!");
                // parsedAge will be 0 here (default) — not garbage, just 0
            }

            // ─────────────────────────────────────────
            // 4. STRING INTERPOLATION (the $ sign)
            // ─────────────────────────────────────────

            // The $ before the string lets you embed variables directly using { }
            // Much cleaner than string concatenation with +

            // Old way (concatenation):
            Console.WriteLine("Hello " + name + "! Your age is " + age);

            // New way (interpolation) — same result, much more readable:
            Console.WriteLine($"Hello {name}!");
            Console.WriteLine($"Your age is {age}");

            // You can even put expressions inside { }
            Console.WriteLine($"In 10 years you will be {age + 10}");
            Console.WriteLine($"Name in uppercase: {name.ToUpper()}");

            // \n inside the string = newline character (moves to next line)
            Console.WriteLine($"\nHello {name}!");   // blank line printed before Hello

            // ─────────────────────────────────────────
            // 5. READING MULTIPLE INPUTS
            // ─────────────────────────────────────────

            Console.Write("Enter your city: ");
            string city = Console.ReadLine();

            Console.Write("Enter your salary: ");
            double salary = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine($"{name} lives in {city} and earns {salary:C}");
            // :C inside { } formats the number as currency → ₹1,00,000.00 (based on system locale)
            // :F2 → fixed 2 decimal places → 1234.57
            // :N0 → number with commas, no decimals → 1,234

            // ─────────────────────────────────────────
            // 6. QUICK REFERENCE
            // ─────────────────────────────────────────
            // Console.Write()         → print, stay on same line
            // Console.WriteLine()     → print, move to next line
            // Console.ReadLine()      → read user input as STRING
            // Convert.ToInt32()       → string → int  (safe with null)
            // Convert.ToDouble()      → string → double
            // int.Parse()             → string → int  (crashes on null)
            // int.TryParse()          → string → int  (safest, no crash)
            // $"Hello {variable}"     → string interpolation
            // \n                      → newline character inside a string

            Console.ReadKey();
        }
    }
}

