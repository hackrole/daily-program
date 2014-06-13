#import <Foundation/Foundation.h>

@interface Sample:NSObject

- (int *) getRandom;

@end

@implementation Sample

- (int *) getRandom{
  static int r[10];
  int i;

  srand((unsigned)time(NULL));
  for(i=0; i < 10; ++i){
    r[i] = rand();
    NSLog(@"r[%d] = %d\n", i, r[i]);
  }

  return r;
}

@end

int main(){
  int *p;
  int i;

  Sample * sample = [[Sample alloc] init];
  p = [sample getRandom];
  for(i = 0; i < 10; i++){
    NSLog(@"*(p+%d): %d\n", i, *(p+i));
  }

  return 0;
}
