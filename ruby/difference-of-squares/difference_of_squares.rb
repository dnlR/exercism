class Squares
  def initialize(n)
    @numbers = (1..n)
  end

  def square_of_sum
    @numbers.reduce(:+) ** 2
  end

  def sum_of_squares
    @numbers.reduce { |squares_sum, n| squares_sum + n ** 2 }
  end

  def difference
    square_of_sum - sum_of_squares
  end
end