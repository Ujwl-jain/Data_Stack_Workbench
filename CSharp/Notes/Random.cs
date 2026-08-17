using System;

namespace CSharpLearning.Topics
{
    // NOTE: class name "Random" conflicts with System.Random — renamed to avoid the clash
    // Rule: never name your class the same as a built-in C# class
    class RandomNumbers
    {
        public static void Run()
        {
            // ─────────────────────────────────────────
            // 1. CREATING A RANDOM OBJECT
            // ─────────────────────────────────────────

            // Random is a CLASS in C# — you must create an object (instance) of it first
            // Think of it as a "dice machine" — you build the machine once, then use it many times
            Random random = new Random();

            // IMPORTANT: create ONE Random object and reuse it
            // If you create a new Random() inside a loop, you may get the same number
            // repeatedly because they get the same seed (time-based)

            // ─────────────────────────────────────────
            // 2. random.Next() — RANDOM INTEGERS
            // ─────────────────────────────────────────

            // random.Next(min, max)
            // min → INCLUSIVE (can appear in results)
            // max → EXCLUSIVE (will never appear in results)

            int num1 = random.Next(1, 7);   // simulates a dice roll → 1, 2, 3, 4, 5, or 6 (never 7)
            int num2 = random.Next(1, 7);   // another dice roll — independent of num1
            Console.WriteLine(num1);
            Console.WriteLine(num2);

            // More examples:
            int coin = random.Next(0, 2);       // 0 or 1 → simulate a coin flip
            int percent = random.Next(0, 101);  // 0 to 100 → random percentage
            int negNum = random.Next(-10, 11);  // -10 to 10 → includes negatives

            // random.Next() with NO arguments → returns any non-negative int (0 to ~2 billion)
            int anyNum = random.Next();

            // random.Next(max) with ONE argument → 0 to max-1
            int zeroToFour = random.Next(5);    // 0, 1, 2, 3, or 4

            // ─────────────────────────────────────────
            // 3. random.NextDouble() — RANDOM DECIMALS
            // ─────────────────────────────────────────

            // Always returns a double between 0.0 (inclusive) and 1.0 (exclusive)
            double num = random.NextDouble();   // e.g. 0.3847261...
            Console.WriteLine(num);

            // To get a decimal in a custom range, scale it manually:
            // Formula: min + (random.NextDouble() * (max - min))

            double zeroToTen = random.NextDouble() * 10;          // 0.0 to 9.999...
            double fiveToTen = 5 + random.NextDouble() * 5;       // 5.0 to 9.999...
            double anyDecimal = -1 + random.NextDouble() * 2;     // -1.0 to 0.999...

            // ─────────────────────────────────────────
            // 4. SEEDING — CONTROLLING "RANDOMNESS"
            // ─────────────────────────────────────────

            // By default, Random uses the current time as a seed
            // Same seed → same sequence of numbers every time (useful for testing)

            Random seeded = new Random(42);     // seed = 42
            Console.WriteLine(seeded.Next(1, 100));  // always the same number when seed is 42
            Console.WriteLine(seeded.Next(1, 100));  // next in the fixed sequence

            // Use case: game replays, unit tests, reproducible simulations

            // ─────────────────────────────────────────
            // 5. PRACTICAL EXAMPLE — DICE GAME
            // ─────────────────────────────────────────

            Random dice = new Random();
            int player1 = dice.Next(1, 7);
            int player2 = dice.Next(1, 7);

            Console.WriteLine($"Player 1 rolled: {player1}");
            Console.WriteLine($"Player 2 rolled: {player2}");

            if (player1 > player2)
                Console.WriteLine("Player 1 wins!");
            else if (player2 > player1)
                Console.WriteLine("Player 2 wins!");
            else
                Console.WriteLine("It's a tie!");

            // ─────────────────────────────────────────
            // 6. QUICK REFERENCE
            // ─────────────────────────────────────────
            // new Random()            → create random object (do once, reuse)
            // new Random(seed)        → fixed seed for reproducible results
            // random.Next()           → any non-negative int
            // random.Next(max)        → 0 to max-1
            // random.Next(min, max)   → min (inclusive) to max (exclusive)
            // random.NextDouble()     → 0.0 (inclusive) to 1.0 (exclusive)
            // min + NextDouble()*(max-min) → decimal in custom range

            Console.ReadKey();
        }
    }
}