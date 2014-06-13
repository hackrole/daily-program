#import <Foundation/Foundation.h>

int * getRandom(){
  static int r[10];
  int i;

  srand( (unsigned)time(NULL) );
  for(i=0; i<10; i++){
    r[i] = rand();
    NSLog(@"%d\n", r[i]);
  }

  return r;
}


int main(){
  int *p;
  int i;

  p = getRandom();
  for(i=0; i<10; i++){
    NSLog(@"(p + [%d]: %d)\n", i, *(p+i));
  }

  return 0;
}
