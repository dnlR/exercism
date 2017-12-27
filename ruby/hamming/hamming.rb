class Hamming
  def self.compute(first_dna_strand, second_dna_strand)
    if first_dna_strand.length != second_dna_strand.length then
      raise ArgumentError.new("DNA strands must have the same length")
    end

    difference_count = 0

    first_dna_strand.each_char.with_index(0) do |c, i|
      if second_dna_strand[i] != c then
        difference_count += 1
      end
    end

    difference_count
  end
end