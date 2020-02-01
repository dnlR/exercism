public static class Pangram
{
    public static bool IsPangram(string input)
    {
        string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        input = input.ToUpper();

        foreach (var letter in alphabet)
        {
            if (!input.Contains(letter))
            {
                return false;
            }
        }

        return true;
    }
}
