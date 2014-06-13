#import <Foundation/Foundation.h>

@interface Sample:NSObject

- (double) getAverage:(int[]) arr andSize:(int) size;

@end

@implementation Sample

- (double) getAverage:(int []) arr andSize:(int) size{
  int i;
  double avg;
  double sum = 0;

  for(i = 0; i < size; i++){
    sum += arr[i];
  }

  avg = sum / size;

  return avg;
}

@end


int main(){
  int balance[5] = {1000, 2, 3, 17, 50};
  double avg;

  Sample *sample = [[Sample alloc] init];
  avg = [sample getAverage:balance andSize:5];

  NSLog(@"Average value is: %f", avg);

  return 0;
}
