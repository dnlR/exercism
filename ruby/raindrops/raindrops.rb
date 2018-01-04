class Raindrops
  def self.convert(number)
    raindrop_sound = ''

    (1..number).each do |factor|
      raindrop_sound += 'Pling' if number % factor == 0 and factor == 3
      raindrop_sound += 'Plang' if number % factor == 0 and factor == 5
      raindrop_sound += 'Plong' if number % factor == 0 and factor == 7
    end

    raindrop_sound.empty? ? number.to_s : raindrop_sound
  end
end