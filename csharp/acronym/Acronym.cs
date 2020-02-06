using System;
using System.Linq;

public static class Acronym
{
    public static string Abbreviate(string phrase)
    {
        char[] splitters = {' ', '_', '-'};
        var phraseWords = phrase.Split(splitters, StringSplitOptions.RemoveEmptyEntries);

        return phraseWords
            .Aggregate(string.Empty, (acronym, word) => acronym + char.ToUpperInvariant(word[0]));
    }
}