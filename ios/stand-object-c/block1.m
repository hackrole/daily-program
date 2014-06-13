#import <Foundation/Foundation.h>

typedef void (^CompletionBlock)();
@interface Sample:NSObject
- (void)performActionWithCompletion:(CompletionBlock)completionBlock;
@end

@implementation Sample

- (void) performActionWithCompletion:(CompletionBlock)completionBlock{
  NSLog(@"Aciton Performed");
  completionBlock();
}

@end

int main(){
  Sample * sample = [[Sample alloc] init];
  [sample performActionWithCompletion:^{
    NSLog(@"Completion is called to intimate action is performed");
  }];

  return 0;
}
