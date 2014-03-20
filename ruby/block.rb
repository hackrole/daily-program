# -*- coding: utf-8 -*-
def three_times
  yield
  yield
  yield
end

def fib_up_to(max)
  i1, i2 = 1, 1
  while i1 <= max
    yield i1
    i1, i2 = i2, i1+i2
  end
end

class Array
  def find
    for i in 0...size
      value = self[i]
      return value if yield value
    end
    return nil
  end
end


if __FILE__ == $0
  three_times { puts "hello"}
  
  fib_up_to(1000) { |f| print f, " "}
  [1, 2, 3, 4].each { |i| puts i}
  
  a =  [1, 2, 3, 4].collect {|x| x+1}
  puts a.class
  puts [1, 2, 3, 4].inject(0) {|sum, element| sum+element}
  puts [1, 2, 3, 4].inject(1) {|pro, element| pro*element}

# 事物block
  class File
    def File.open_and_process(*args)
      f = File.new(*args)
      yield f
      f.close()
    end
    def File.mysql(*args)
      result = file = File.new(*args)
      if block_given?
        resutl = yield file
        file.close
      end
      return result
    end
  end
  File.open_and_process('/home/daipeng/Desktop/tmp/t.py', 'r') do |file|
    while line = file.gets
      puts line
    end
  end
end
