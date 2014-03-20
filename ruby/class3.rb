class MyClass
  def method1 # default is public
  end
  
  protected
  def method2
  end
  def m2
  end

  private
  def method3
  end
  def m3
  end
end

class M2
  def method1
  end
  def method2
  end
  def method3
  end
  public :method1
  private :method3
  protected :method2, :method3
end

class Accounts
  attr_reader :saveings
  protected :saveings

  def initialize(checking, saveings)
    @checking = checking
    @saveings = saveings
  end
  private
  def debit(account, amount)
    account.balance -= amount
  end
  def credit(account, amount)
    account.balance += amount
  end
  public
  def transfer_to_savings(amount)
    debit(@checking, amount)
    credit(@saveings, amount)
  end
end


if __FILE__ == $0
 a = Accounts.new(112, 300)
 p1 = "TIm"
 p2 = p1
 p1[0] = "J"
 puts p1,p2
 p1 = "Tim"
 p2 = p1.dup
 p1[0] = "J"
 puts p1,p2

end
