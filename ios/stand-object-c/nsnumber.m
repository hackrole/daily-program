#import <Foundation/Foundation.h>

@interface Sample:NSObject

- (NSNumber *) multiplyA:(NSNumber *)a withB:(NSNumber *)b;

@end

@implementation Sample

- (NSNumber *) multiplyA:(NSNumber *)a withB:(NSNumber *)b {
  float number1 = [a floatValue];
  float number2 = [a floatValue];
  float product = number1 * number2;

  NSNumber * result = [NSNumber numberWithFloat:product];
  return result;
}

@end


int main(){
  NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];

  Sample * sample = [[Sample alloc] init];

  NSNumber *a = [NSNumber numberWithFloat:10.5];
  NSNumber *b = [NSNumber numberWithFloat:10.0];
  NSLog(@"a = %d, b= %d", *a, *b);

  NSNumber *result = [sample multiplyA:a withB:b];
  NSString *resultString = [result stringValue];

  NSLog(@"the product is %@", resultString);
  [pool drain];
  return 0;
}
