#import <Foundation/Foundation.h>

const int MAX = 3;

int main(){
  int var[] = {10, 100, 200};
  int i;
  int *ptr[MAX];

  for(i=0; i<MAX; i++){
    ptr[i] = &var[i];
  }

  for(i=0; i<MAX; i++){
    NSLog(@"value of var[%d] = %d\n", *ptr[i]);
  }
  return 0;
}
