#import <Foundation/Foundation.h>

extern int a, b;
extern int c;
extern float f;

int main(int argc, const char * argv[]){
	// variable define
	int a,b;
	int c;
	float f;

	a = 10;
	b = 20;
	c = a + b;
	NSLog(@"value of c: %d\n", c);

	f = 70.0/3.0;
	NSLog(@"value of f: %f\n", f);

	return 0;
}
