#import <Foundation/Foundation.h>


const int MAX = 3;

int main(){
  int var[] = {10, 100, 200};
  int i, *ptr;

  ptr = var;
  for(i=0; i<MAX; i++){
    NSLog(@"Address of var[%d] = %x\n", i, ptr);
    NSLog(@"value of var[%d] = %d\n", i, *ptr);

    ptr++;
  }

  return 0;
}
