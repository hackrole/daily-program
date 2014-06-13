#import <Foundation/Foundation.h>

int main(){
  NSLog(@"file %s\n", __FILE__);
  NSLog(@"date: %s\n", __DATE__);
  NSLog(@"time: %s\n", __TIME__);
  NSLog(@"line %d\n", __LINE__);
  NSLog(@"ansc: %d\n", __STDC__);

  return 0;
}
