#import <Foundation/Foundation.h>

int main(){
  int var;
  int *ptr;
  int **pptr;

  var = 3000;
  ptr = &var;
  pptr = &ptr;

  NSLog(@"Value of var = %d\n", var);
  NSLog(@"value available at *ptr = %d\n", *ptr);
  NSLog(@"value available at **ptr = %d\n", **pptr);

  return 0;
}
