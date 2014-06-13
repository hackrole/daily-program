#import <Foundation/Foundation.h>

struct Books {
  NSString *title;
  NSString *author;
  NSString *subject;
  int book_id;
};

@interface Sample:NSObject

- (void) printBook:(struct Books *) book;

- (struct Books) createBook:(NSString *)title
                    author:(NSString *)author
                    subject:(NSString *)subject
                     book_id:(int)book_id;

@end

@implementation Sample

- (void) printBook:(struct Books *) book{
  NSLog(@"book title: %@\n", book->title);
  NSLog(@"book author: %@\n", book->author);
  NSLog(@"book subject: %@\n", book->subject);
  NSLog(@"book bookid: %d\n", book->book_id);
}

- (struct Books) createBook:(NSString *)title
                    author:(NSString *)author
                    subject:(NSString *)subject
                     book_id:(int)book_id{
  struct Books book;
  book.title = title;
  book.author = author;
  book.subject = subject;
  book.book_id = book_id;
  return book;
}

@end

int main(){
  struct Books book1;
  struct Books book2;
  Sample * sample = [[Sample alloc] init];

  book1 = [sample createBook:@"objc p" author:@"zara" subject:@"objc tut" book_id:1222];
  book2 = [sample createBook:@"tele bill" author:@"Zara ali" subject:@"tele tut" book_id:1444];

  [sample printBook:&book1];
  [sample printBook:&book2];

  return 0;
}
