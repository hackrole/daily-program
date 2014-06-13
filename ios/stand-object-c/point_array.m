#import <Foundation/Foundation.h>

int main(){
  double balance[5] = { 1000.0, 2.0, 3.4, 18.0, 4.2 };
  double *p;
  int i;

  p = balance;

  NSLog(@"Array value using Pointer\n");

  for(i=0; i<5; i++){
    NSLog(@"*(p+%d): %f\n", i, *(p+i));
  }

  NSLog(@"Array values using balance as address\n");
  for(i=0; i<5; i++){
    NSLog(@"*(balance+%d): %f\n", i, *(balance + i));
  }

  return 0;
}
