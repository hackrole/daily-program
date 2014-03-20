class Song
  @@plays = 0
    
  attr_reader :name
  def initialize(name)
    @name = name
    @plays = 0
  end
  def play
    @plays += 1
    @@plays += 1
    puts "the song: #@name plays #@plays, totla #@@plays"
  end
  def Song.is_too_long(song)
    return song.name.length > 5
  end
end

class Logger
  private_class_method :new
  @@logger = nil
  def Logger.get
     @@logger = :nameislie
     @@logger
  end
end

if __FILE__ == $0
    s1 = Song.new("David")
    s2 = Song.new("Tom and Jane")
    s1.play
    s1.play
    s2.play
    puts Song.is_too_long(s1)
    puts Song.is_too_long(s2)

    puts Logger.get.object_id
    puts Logger.get.object_id
end
