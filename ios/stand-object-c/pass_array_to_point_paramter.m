#import <Foundation/Foundation.h>

@interface Sample:NSObject

- (double) getAverage:(int *)arr ofSize:(int) size;

@end

@implementation Sample

- (double) getAverage:(int *)arr ofSize:(int) size{
  int i, sum =0;
  double avg;

  for(i=0; i<size; i++){
    sum += arr[i];
  }

  avg = (double)sum / size;

  return avg;
}

@end

int main(){
  int balance[5] = {1000, 2, 3, 17, 50};
  double avg;

  Sample *sample = [[Sample alloc] init];
  avg = [sample getAverage:balance ofSize:5];

  NSLog(@"Average value is: %f\n", avg);

  return 0;
}
