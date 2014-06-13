#import <Foundation/Foundation.h>

@protocol Print

- (void) process;

@end

@interface PrintClass:NSObject

id delegate;

- (void) printDetails;
- (void) setDelegate:(id)newDelegate;

@end

@implementation PrintClass

- (void) printDetails{
  NSLog(@"Printing details");
  [delegate process];
}

- (void) setDelegate:(id)newDelegate{
  delegate = newDelegate;
}

@end

@interface Sample:NSObject<Print>

- (void)startAction;

@end

@implementation Sample

- (void) startAction{
  PrintClass *printclass = [[PrintClass alloc] init];
  [printclass setDelegate:self];
  [printclass printDetails];
}

- (void)process{
  NSLog(@"Printing process completed");
}

@end


int main(int argc, const char *argv[]){
  NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];

  Sample * sample = [[Sample alloc] init];
  [sample startAction];
  [pool drain];

  return 0;
}
