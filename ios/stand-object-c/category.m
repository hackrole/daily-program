#import <Foundation/Foundation.h>

@interface NSString(MyAddtions)

+ (NSString *) getCopyRightString;

@end

@implementation NSString(MyAddtions)

+ (NSString *) getCopyRightString{
  return @"CopyRight of 2013";
}

@end

int main(int argc, const char *argv[]){
  NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];
  NSString * copy = [NSString getCopyRightString];

  NSLog(@"accessing category: %@", copy);

  [pool drain];
  return 0;
}
