#import <Foundation/Foundation.h>

main(){
	unsigned int a = 60; // 0011 1100
	unsigned int b = 13; // 0000 1101
	int c = 0;

	c = a & b; // 12
	NSLog(@"value of c is %d\n", c);

	c = a | b; // 61
	NSLog(@"value of c is %d\n", c);

	c = a ^ b; // 49
	NSLog(@"value of c is %d\n", c);

	c = ~a; // -61
	NSLog(@"value of c is %d\n", c);

	c = a << 2; // 240
	NSLog(@"value of c is %d\n", c);

	c = a >> 2; // 15
	NSLog(@"value of c is %d\n", c);

	c = a >> 3; // 7
	NSLog(@"value of c is %d\n", c);
}
