#import <Foundation/Foundation.h>


@interface Sample:NSObject
- (void)swap:(int *)num1 andNum2:(int *)num2;
@end

@implementation Sample
- (void)swap:(int *)num1 andNum2:(int *)num2{
	int temp;
	
	temp = *num1;
	*num1 = *num2;
	*num2 = temp;
}
@end


int main(){
	int a = 100;
	int b = 200;

	NSLog(@"before swap a=%d\n", a);
	NSLog(@"before swap b=%d\n", b);

	Sample *sample = [[Sample alloc] init];
	[sample swap:&a andNum2:&b];

	NSLog(@"before swap a=%d\n", a);
	NSLog(@"before swap b=%d\n", b);

	return 0;
}


