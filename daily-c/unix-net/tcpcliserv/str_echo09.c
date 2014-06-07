#include "../lib/unp.h"
#include "sum.h"

void str_echo(int sockfd) {
  ssize_t n;
  struct args arg;
  struct result result;

  for ( ; ; ) {
    if ( (n = Readn(sockfd, &arg, sizeof(arg))) == 0) {
      return;
    }

    result.sum = arg.arg1 + arg.arg2;
    Writen(sockfd, &result, sizeof(result));
  }
}


