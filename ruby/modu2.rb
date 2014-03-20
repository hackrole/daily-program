module Debug
  def who_am_i?
    "#{self.class.name}  #{self.to_s}"
  end
end

class Ph
  include Debug
end
class Hi
  include Debug
end

if __FILE__ == $0
  ph = Ph.new
  hi = Hi.new
  puts ph.who_am_i?
  puts hi.who_am_i?
  
  module Ob
    def ob
      @ob = 2
    end
    def ob=(ob=2)
      @ob = ob
    end
  end
  class T
    include Ob
  end
  t = T.new
  puts t.ob
  t.ob = 10
  puts t.ob
end
