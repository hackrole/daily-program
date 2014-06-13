#import <Foundation/Foundation.h>

@interface SampleClass:NSObject
- (void)swap: (int)num1 andNum2:(int)num2;
@end

@implementation SampleClass
- (void)swap: (int)num1 andNum2:(int)num2{
	int temp;
	temp = num1;
	num1 = num2;
	num2 = temp;
}
@end

int main(){
	int a = 100;
	int b = 200;

	SampleClass *sampleClass = [[SampleClass alloc] init];

	NSLog(@"before swap ,value of a: %d\n", a);
	NSLog(@"before swap ,value of b: %d\n", b);

	[sampleClass swap:a andNum2:b];

	NSLog(@"after swap ,value of a: %d\n", a);
	NSLog(@"after swap ,value of b: %d\n", b);

	return 0;
}
