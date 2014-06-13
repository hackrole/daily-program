#import <Foundation/Foundation.h>

@interface Sample:NSObject

- (void) getSeconds:(int *)ptr;

@end

@implementation Sample

- (void) getSeconds:(int *)ptr{
  *ptr = time(NULL);
}

@end

int main(){
  int sec = 0;

  Sample *sample = [[Sample alloc] init];
  [sample getSeconds:&sec];

  NSLog(@"Number of seconds:%d\n", sec);
  return 0;
}
