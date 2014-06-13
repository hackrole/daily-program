#import <Foundation/Foundation.h>

#define LEN 10
#define WD 5
#define NEWLINE '\n'

int main(int argc, const char * argv[]){
	int area;

	area = LEN * WD;
	NSLog(@"value of area: %d", area);
	NSLog(@"%c", NEWLINE);

	return 0;
}
