class Song
  def initialize(name, artist, duration)
     @name = name
     @artist = artist
     @duration = duration
  end
end

class Song
  attr_writer :artist
  def to_s
    "Song: #@name -- #@artist {#@duration}"
  end

  def name
    @name
  end
  def artist
    @artist
  end
  def name=(newname)
    @name = newname
  end
  def name_false
    "not the really name"
  end
end

class KSong < Song
  attr_reader :lyr, :duration

  def initialize(name, artist, duration, lyr)
    super(name, artist, duration)
    @lyr = lyr
  end
  def to_s
     super + "[#{@lyr}]"
  end
end

if __FILE__ == $0
  song = Song.new("bicy", "plack", 260)
  puts song.inspect
  puts song.to_s
  puts song.name
  song.name = "new bicy"
  puts song.name
  song.artist = "new plack"
  puts song.artist
  puts song.name_false

  ksong = KSong.new("May", "sinal", 225, "And now, then..")
  puts ksong.to_s
  puts ksong.duration
  puts ksong.name
  puts ksong.lyr
end
