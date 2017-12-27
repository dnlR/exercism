class Hamming
  def self.compute(first_dna_strand, second_dna_strand)
    raise ArgumentError unless first_dna_strand.length == second_dna_strand.length
    first_dna_strand.chars.zip(second_dna_strand.chars).count { |l, r| l != r }
  end
end