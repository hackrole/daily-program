#import <Foundation/Foundation.h>

struct Books {
  NSString *title;
  NSString *author;
  NSString *subject;
  int book_id;
};


int main(){
  struct Books book1;
  struct Books book2;

  book1.title = @"Object-c programming";
  book1.author = @"Nuha Ali";
  book1.subject = @"Object-c pragramming tutorail";
  book1.book_id = 6495407;

  book2.title = @"tele billing";
  book2.author = @"zara ali";
  book2.subject = @"tele billing tutorial";
  book2.book_id = 5322;

  NSLog(@"book 1 title: %@\n", book1.title);
  NSLog(@"book 1 author: %@\n", book1.author);
  NSLog(@"book 1 subject: %@\n", book1.subject);
  NSLog(@"book1 bookid: %d\n", book1.book_id);

  NSLog(@"book 2 title: %@\n", book2.title);
  NSLog(@"book 2 author: %@\n", book2.author);
  NSLog(@"book 2 subject: %@\n", book2.subject);
  NSLog(@"book2 bookid: %d\n", book2.book_id);

  return 0;
}
