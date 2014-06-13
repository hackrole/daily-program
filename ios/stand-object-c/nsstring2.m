#import <Foundation/Foundation.h>

int main(){
  NSString *str1 = @"Hello";
  NSString *str2 = @"World";
  NSString *str3;
  int len;

  NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];

  str3 = [str2 uppercaseString];
  NSLog(@"uppercaseString: %@\n", str3);

  str3 = [str1 stringByAppendingFormat:@"World"];
  NSLog(@"concatenated string: %@\n", str3);

  len = [str3 length];
  NSLog(@"length of str3: %d\n", len);

  str3 = [[NSString alloc] initWithFormat:@"%@ %@", str1, str2];
  NSLog(@"using initwithformat: %@\n", str3);

  [pool drain];

  return 0;
}
