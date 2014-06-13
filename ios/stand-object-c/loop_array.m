#import <Foundation/Foundation.h>

const int MAX = 3;

int main(){
  int var[] = {10, 100, 299};
  int i;

  for(i=0; i<MAX; i++){
    NSLog(@"value of var[%d] = %d\n", i, var[i]);
  }

  return 0;
}
