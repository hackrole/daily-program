#import <Foundation/Foundation.h>

int main(){
  int var1;
  char var2[10];

  NSLog(@"address of var1: %x\n", &var1);
  NSLog(@"address of var2: %x\n", &var2);

  return 0;
}
