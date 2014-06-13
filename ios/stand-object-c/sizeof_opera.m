#import <Foundation/Foundation.h>

main(){
	int a = 4;
	short b;
	double c;
	int* ptr;

	NSLog(@"size of varibale a = %d\n", sizeof(a));
	NSLog(@"sizeof varibale b = %d\n", sizeof(b));
	NSLog(@"sizeof varibale c = %d\n", sizeof(c));
	NSLog(@"sizeof varibale ptr = %d\n", sizeof(ptr));

	ptr = &a;
	NSLog(@"varibale a = %d\n", a);
	NSLog(@"varibale *ptr = %d\n", *ptr);
	NSLog(@"varibale ptr = %d\n", ptr);

	a = 10;
	b = (a==1)?20:30;
	NSLog(@"value of b is %d\n", b);

	a = 10;
	b = (a==10)?20:30;
	NSLog(@"value of b is %d\n", b);
}
