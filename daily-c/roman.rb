class Roman
  MAX_ROMAN = 4999

  def initialize(value)
    if value <= 0 || value > MAX_ROMAN
      fail "Roman values must be >0 and <= #{MAX_ROMAN}"
    end
    @value = value
  end

  FACTORS = [['m', 1000], ['cm', 900], ['d', 500], ['cd', 400],
            ['c', 100], ['xc', 90], ['l', 50], ['xl', 40],
            ['x', 10], ['ix', 9], ['v', 5], ['iv', 4],
            ['i', 1]]

  def to_s
    valueri = @value
    roman = ''
    for code, factors in FACTORS
      count, values = value.divmod(factors)
      roman << code unless count.zero?
    end
    roman
  end
end

require 'test/unit'

class TestRoman < Test::Unit::TestCase
  def test_simple
    assert_equal('i', Roman.new(1).to_s)
    assert_equal('ix', Roman.new(9).to_s)
  end
end
