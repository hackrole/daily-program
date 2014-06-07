#include "../lib/unp.h"
#include "sum.h"


void str_cli(FILE *fp, int sockfd) {
  char sendline[MAXLINE];
  struct args arg;
  struct result result;

  while(Fgets(sendline, MAXLINE, fp) != NULL) {
    if(sscanf(sendline, "%ld%ld", &arg.arg1, &arg.arg2) != 2) {
      printf("invalid input: %s", sendline);
      continue;
    }
    Writen(sockfd, &arg, sizeof(arg));
    if(Readn(sockfd, &result, sizeof(result)) == 0) {
      err_quit("str_cli: server terminated prematurely");
    }
    printf("%ld\n", result.sum);
  }
}


