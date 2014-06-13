#import <Foundation/Foundation.h>

@interface Sample:NSObject

{
  NSString *name;
}

- (void)setInternalID;
- (NSString *)getExternalID;

@end


@interface Sample()
{
  NSString * internalID;
}

@end

@implementation Sample

- (void)setInternalID{
  internalID = [NSString stringWithFormat:
    @"unique inter %d unique key", arc4random()%100];
}

- (NSString *)getExternalID{
  return [internalID stringByReplacingOccurrencesOfString:
      @"unique key" withString:@""];
}

@end

int main(int argc, const char *argv[]){
  NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];

  Sample *sample = [[Sample alloc] init];
  [sample setInternalID];

  NSLog(@"ExternalID: %@", [sample getExternalID]);
  [pool drain];

  return 0;
}
