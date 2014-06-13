#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]){
	const int LEN = 10;
	const int WD = 5;
	const char NEWLINE = '\n';
	int area;

	area = LEN * WD;
	NSLog(@"value of area: %d", area);
	NSLog(@"%c", NEWLINE);

	return 0;
}
