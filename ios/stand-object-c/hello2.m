#import <Foundation/Foundation.h>

@interface SampleClass:NSObject
- (void)sampleMethod;
@end

@implementation SampleClass

- (void)sampleMethod{
	NSLog(@"hello, world! \n");
}

@end

// hello world
/* 
 * hello world
 */
int main(int argc, const char * argv[]){
	SampleClass *sampleClass = [[SampleClass alloc] init];
	[sampleClass sampleMethod];
	return 0;
}
