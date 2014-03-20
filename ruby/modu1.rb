module Trig

  PI = 3.14
  
  def Trig.sin(s)
  end
  
  def Trig.cos(s)
  end
end

module Moral
  V = 0
  def Moral.sin(n)
  end
end

if __FILE__ == $0
  puts Trig::PI
  Trig.sin(3)
  Moral::V
  Moral.sin(2)
end
