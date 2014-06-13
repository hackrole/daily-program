#import <Foundation/Foundation.h>

#define mfor(a, b) \
  NSLog(@#a " and " #b ": we love you!\n");

#define token(n) NSLog(@"totekn"#n" = %d", token##n)

#define MAX(x, y) ((x) > (y) ? (x):(y))

int main(){
  int token34 = 40;

  mfor(Carlos, Debra);
  token(34);

  NSLog(@"max between 20 and 10 is %d\n", MAX(10, 20));

  return 0;
}
