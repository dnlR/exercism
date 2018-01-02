class Complement
  @@conversions = { 'G' => 'C', 'C' => 'G', 'T' => 'A', 'A' => 'U' }

  def self.of_dna(dna)
    dna.chars.inject("") do |rna, c|
      if @@conversions.key?(c) then
        rna << @@conversions[c]
      else
        return ""
      end
    end
  end
end