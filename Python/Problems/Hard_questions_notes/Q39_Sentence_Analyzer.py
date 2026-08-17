# =============================================================================
# Q39 [Medium] - Sentence Analyzer
# Count words, characters (no spaces), and sentences (count periods)
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Take a sentence and return:
#   - Number of WORDS       → split by space → count elements
#   - Number of CHARACTERS  → count everything except spaces
#   - Number of SENTENCES   → count periods


# -----------------------------------------------------------------------------
# 🧠 LOGIC
# -----------------------------------------------------------------------------
# 1. Split sentence by '.' → subtract 1 for sentence count
# 2. Split sentence by ' ' → get words list → len = word count
# 3. Loop through words → loop through chars → count all chars
# 4. Return all three counts


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPTS
# -----------------------------------------------------------------------------
# 1. len(sen.split('.')) - 1  →  split adds extra empty string at end!
#      "Hi. Bye."  →  ['Hi', ' Bye', '']  →  len=3, sentences=2 → -1 needed!
#
# 2. count_word = len(words)  NOT len(sen)
#      len(sen)   = number of CHARACTERS in string ❌
#      len(words) = number of WORDS in list         ✅
#
# 3. Splitting by space already ignores spaces — no extra check needed!
#      "Hi i am".split(' ') → ['Hi', 'i', 'am'] → spaces gone automatically!
#
# 4. 'ujjwal.' counts as one word — period is attached, no space between!
#      Question only says count words, not clean them.


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

def sen_checker(sen):
    count_sentence = len(sen.split('.')) - 1   # -1 for empty string at end!
    words = sen.split(' ')
    count_word = len(words)                    # len of LIST not string!
    count_char = 0
    for word in words:
        for char in word:
            count_char += 1                    # spaces already removed by split!

    return count_char, count_sentence, count_word


sen = 'Hi i am ujjwal. i am 24 year old. I may need to take a leave on 3rd april.'
result_char, result_sen, result_word = sen_checker(sen)
print(f"Words: {result_word} | Chars: {result_char} | Sentences: {result_sen}")


# -----------------------------------------------------------------------------
# 🧪 DRY RUN  |  sen = "Hi. Bye."
# -----------------------------------------------------------------------------
#
#  count_sentence = len(["Hi", " Bye", ""]) - 1 = 3 - 1 = 2  ✅
#  words          = ["Hi.", "Bye."]
#  count_word     = 2  ✅
#  count_char:
#    word="Hi."  → H,i,. → 3
#    word="Bye." → B,y,e,. → 4
#    total = 7  ✅


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. split('.') always adds empty string at end → always -1 for period count
# 2. len(list) for word count, NOT len(string)!
# 3. Splitting by space removes spaces — no extra loop needed
# 4. Attached punctuation ('ujjwal.') counts as part of the word — acceptable!
