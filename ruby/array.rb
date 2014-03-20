class SongList
  def initialize
    @songs = []
  end
  def append(song)
    @songs.push(song)
    self
  end
  
  def delete_first
    @songs.shift
  end
  def delete_last
    @songs.pop
  end

  def [](index)
    @songs[index]
  end

  def with_title(title)
    for i in 0...@songs.length
      return @songs[i] if title == @songs[i]
    end
    return nil
  end

  def with_title2(title)
    @songs.find { |song| title == song}
  end
      
end


if __FILE__ == $0
  require "test/unit"

  class TestSongList < Test::Unit::TestCase
    def test_delete
      list = SongList.new
      s1 = "title"
      s2 = "title2"
      s3 = "hello"
      s4 = "world"
      
      list.append(s1).append(s2).append(s3).append(s4)
      assert_equal(s1, list[0])
      assert_equal(s3, list[2])
      assert_equal(s3, list.with_title(s3))
      assert_equal(s3, list.with_title2(s3))
      assert_nil(nil, list.with_title("time"))
      assert_nil(nil, list.with_title2('time'))
      assert_nil(list[9])
      
      assert_equal(s1, list.delete_first)
      assert_equal(s2, list.delete_first)
      assert_equal(s4, list.delete_last)
      assert_equal(s3, list.delete_last)

    end
  end
end
