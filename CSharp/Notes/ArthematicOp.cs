using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpLearning.Topics
{
    class ArthematicOp
    {
        public static void Run()
        {
            int friends = 5;

            // ─────────────────────────────────────────
            // 1. BASIC INCREMENT / DECREMENT
            // ─────────────────────────────────────────

            // Longhand way
            friends = friends + 1;  // add 1
            friends = friends - 1;  // subtract 1

            // Shorthand (compound assignment) — same result
            friends += 2;  // friends = friends + 2
            friends -= 1;  // friends = friends - 1

            // Increment / Decrement by exactly 1 (common in loops)
            friends++;  // friends = friends + 1
            friends--;  // friends = friends - 1

            // NOTE: prefix vs postfix matters inside expressions
            // int a = ++friends; → increments FIRST, then assigns (pre-increment)
            // int b = friends++; → assigns FIRST, then increments (post-increment)

            // ─────────────────────────────────────────
            // 2. MULTIPLICATION & DIVISION
            // ─────────────────────────────────────────

            friends = friends * 2;  // longhand
            friends *= 2;           // shorthand

            // Integer division — decimal part is DROPPED (truncated, not rounded)
            friends = friends / 2;  // e.g. 5 / 2 = 2, not 2.5
            friends /= 2;

            // To get a decimal result, at least one operand must be double/float
            double result = 5.0 / 2;    // → 2.5  ✓
            double result2 = (double)5 / 2; // cast also works → 2.5  ✓

            // ─────────────────────────────────────────
            // 3. MODULUS (REMAINDER)
            // ─────────────────────────────────────────

            int dost = 10;
            int remainder = dost % 3;  // 10 ÷ 3 = 3 remainder 1  → remainder = 1
            Console.WriteLine(remainder); // Output: 1

            // Common use: check if a number is even or odd
            // if (number % 2 == 0) → even
            // if (number % 2 != 0) → odd

            // ─────────────────────────────────────────
            // 4. MATH CLASS METHODS
            // ─────────────────────────────────────────

            double x = 3.0;
            double y = -5.7;

            // Math.Pow(base, exponent) — raises base to the power of exponent
            double powered = Math.Pow(x, 3);     // 3³ = 27
            double powered2 = Math.Pow(2, 10);   // 2¹⁰ = 1024

            // Math.Sqrt(n) — square root of n
            double squareRoot = Math.Sqrt(x);    // √3 ≈ 1.732
            double squareRoot2 = Math.Sqrt(16);  // √16 = 4

            // Math.Abs(n) — absolute value, converts negative to positive
            double absolute = Math.Abs(y);       // |-5.7| = 5.7
            double absolute2 = Math.Abs(-100);   // 100

            // Math.Round(n) — rounds to nearest whole number
            // Rule: .5 rounds to nearest EVEN number (banker's rounding in C#)
            double rounded = Math.Round(3.5);    // → 4
            double rounded2 = Math.Round(2.5);   // → 2 (nearest even!)
            double rounded3 = Math.Round(3.7);   // → 4

            // Math.Round with decimal places
            double rounded4 = Math.Round(3.14159, 2); // → 3.14

            // Math.Ceiling(n) — always rounds UP to next whole number
            double ceiling = Math.Ceiling(3.1);  // → 4
            double ceiling2 = Math.Ceiling(3.9); // → 4
            double ceiling3 = Math.Ceiling(-3.1);// → -3 (less negative = up)

            // Math.Floor(n) — always rounds DOWN to previous whole number
            double floor = Math.Floor(3.9);      // → 3
            double floor2 = Math.Floor(3.1);     // → 3
            double floor3 = Math.Floor(-3.1);    // → -4 (more negative = down)

            // Math.Max(a, b) — returns the LARGER of two values
            double max = Math.Max(10, 20);        // → 20
            double max2 = Math.Max(-5, -1);       // → -1

            // Math.Min(a, b) — returns the SMALLER of two values
            double min = Math.Min(10, 20);        // → 10
            double min2 = Math.Min(-5, -1);       // → -5

            // ─────────────────────────────────────────
            // 5. QUICK REFERENCE TABLE
            // ─────────────────────────────────────────
            // Operator  | Meaning          | Example          | Result
            // +         | Addition         | 5 + 3            | 8
            // -         | Subtraction      | 5 - 3            | 2
            // *         | Multiplication   | 5 * 3            | 15
            // /         | Division         | 5 / 2 (int)      | 2  ← truncates!
            // /         | Division         | 5.0 / 2 (double) | 2.5
            // %         | Modulus          | 10 % 3           | 1
            // ++        | Increment by 1   | friends++        | friends + 1
            // --        | Decrement by 1   | friends--        | friends - 1

            Console.ReadKey();
        }
    }
}
