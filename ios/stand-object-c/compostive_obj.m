#import <Foundation/Foundation.h>

@interface ValidatingArray:NSMutableArray

{
  NSMutableArray *em_arr;
}

+ validatingArray;
- init;
- (unsigned) count;
- objectAtIndex:(unsigned)index;
- (void)addObject:object;
- (void)replaceObjectAtIndex:(unsigned)index withObject:object;
- (void)removeLastObject;
- (void)insertObject:object atIndex:(unsigned)index;
- (void)removeObjectAtIndex:(unsigned)index;

@end

@implementation ValidatingArray

- init{
  self = [super init];
  if(self){
    em_arr = [[NSMutableArray allocWithZone:[self zone]] init];
  }
  return self;
}

+ validatingArray{
  return [[self alloc] init];
}

- (unsigned)count{
  return [em_arr count];
}

- objectAtIndex:(unsigned)index{
  return [em_arr objectAtIndex:index];
}

- (void)addObject:(id)object{
  if(object != nil){
    [em_arr addObject:object];
  }
}

- (void)replaceObjectAtIndex:(unsigned)index withObject:(id)object{
  if(index < [em_arr count] && object != nil){
    [em_arr replaceObjectAtIndex:index withObject:object];
  }
}

- (void)removeLastObject{
  if([em_arr count] > 0){
    [em_arr removeLastObject];
  }
}

- (void)insertObject:(id)object atIndex:(unsigned)index{
  if(object != nil){
    [em_arr insertObject:object atIndex:index];
  }
}

- (void)removeObjectAtIndex:(unsigned)index{
  if(index < [em_arr count]){
    [em_arr removeObjectAtIndex:index];
  }
}

@end

int main(){
  NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];

  ValidatingArray * validatingArray = [[ValidatingArray  alloc] init];
  [validatingArray addObject:@"Object1"];
  [validatingArray addObject:@"object2"];
  [validatingArray addObject:[NSNull null]];
  [validatingArray removeObjectAtIndex:2];

  NSString *astring = [validatingArray objectAtIndex:1];
  NSLog(@"the value at index 1 is %@", astring);

  [pool drain];
  return 0;
}
