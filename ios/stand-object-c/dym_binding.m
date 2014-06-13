#import <Foundation/Foundation.h>

@interface Square:NSObject

{
  float area;
}

- (void) getArea:(CGFloat)side;
- (void) printArea;

@end

@implementation Square

- (void)getArea:(CGFloat)side{
  area = side * side;
}

- (void)printArea{
  NSLog(@"the area of square is %f", area);
}

@end

@interface Rectangle:NSObject

{
  float area;
}

- (void) getArea:(CGFloat)side andBreadth:(CGFloat)breadth;
- (void) printArea;

@end

@implementation Rectangle

- (void) getArea:(CGFloat)length andBreadth:(CGFloat)breadth{
  area = length * breadth;
}

- (void) printArea{
  NSLog(@"the area of rectangle is %f", area);
}

@end

int main(){
  Square *squ = [[Square alloc] init];
  [squ getArea:10.0];
  Rectangle * rect = [[Rectangle alloc] init];
  [rect getArea:10.0 andBreadth:5.0];

  NSArray *shapes = [[NSArray alloc] initWithObjects:squ, rect, nil];
  id obj1 = [shapes objectAtIndex:0];
  [obj1 printArea];
  id obj2 = [shapes objectAtIndex:1];
  [obj2 printArea];

  return 0;
}
