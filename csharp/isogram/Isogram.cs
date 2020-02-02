using System;
using System.Collections.Generic;
using System.Linq;

public static class Isogram
{
    public static bool IsIsogram(string word)
    {
        var hs = new HashSet<char>();
        return word
            .Where(char.IsLetter)
            .Select(char.ToLowerInvariant)
            .All(hs.Add);
    }
}
